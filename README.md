# Practica Azure-GitLab
## Autores
> David Jesús Cerdeiro Gallardo

> Raul Ariza López
## Explicación de los ficheros y configuraciones
### azure-pipelines.yml - Práctica 1, sección 3.4
```yaml
trigger:
  branches:
    include:
      - main
      
pool:
  vmImage: 'ubuntu-latest'

steps:
  - script: echo 'Starting Docker Build and Compose'
    displayName: 'Starting Docker Build and Compose'

  - task: Docker@2
    displayName: 'Build Docker Image'
    inputs:
      command: 'build'
      Dockerfile: '**/Dockerfile'
      tags: 'latest'

  - task: Docker@2
    displayName: 'Push Docker Image to Registry'
    inputs:
      command: 'push'
      tags: 'latest'
      containerRegistry: 'practicaVS'

  - task: Docker@2
    displayName: 'Docker Compose Up'
    inputs:
      command: 'composeUp'
      dockerComposeFile: '**/docker-compose.yml'
      removeContainersOnPull: true
      detachedService: true

```
Comencemos con la sección **trigger**:
```yaml
trigger:
  branches:
    include:
      - main
      
```
La cual especifica cuando debe ejecutarse este pipeline. Tal como lo hemos definido, se ejecutará cuando realicemos un cambio en la rama principal, ***main***.

Siguiendo, nos encontramos con la sección **pool**:
```yaml
pool:
  vmImage: 'ubuntu-latest'   
```
Aquí vamos a definir la máquina virtual en la que se va a ejecutar los pasos del *Pipeline*, que en este caso, se utiliza la imagen "*ubuntu-latest*".

La última sección de este archivo será de la de **steps**:
```yaml
steps:
  - script: echo 'Starting Docker Build and Compose'
    displayName: 'Starting Docker Build and Compose'

  - task: Docker@2
    displayName: 'Build Docker Image'
    inputs:
      command: 'build'
      Dockerfile: '**/Dockerfile'
      tags: 'latest'

  - task: Docker@2
    displayName: 'Push Docker Image to Registry'
    inputs:
      command: 'push'
      tags: 'latest'
      containerRegistry: 'practicaVS'

  - task: Docker@2
    displayName: 'Docker Compose Up'
    inputs:
      command: 'composeUp'
      dockerComposeFile: '**/docker-compose.yml'
      removeContainersOnPull: true
      detachedService: true
```
Donde vamos a definir la secuencia de pasos que se ejecutarán en el *Pipeline*, dividamos esto por bloques:
```yaml
  - script: echo 'Starting Docker Build and Compose'
    displayName: 'Starting Docker Build and Compose'
```
Primero mostraremos el mensaje "*Starting Docker Build and Compose*" por consola mediante el comando "*echo*".

En la segunda línea, mediante *displayName*, lo que haremos es proporcionar un nombre para este paso en la interfaz del usuario de Azure.

```yaml
  - task: Docker@2
    displayName: 'Build Docker Image'
    inputs:
      command: 'build'
      Dockerfile: '**/Dockerfile'
      tags: 'latest'
```
En la primera línea indicamos que vamos a utlizar la tarea Docker de la versión 2 en el pipeline, tras esto, al igual que hemos realizado anteriormente, mediante *displayName*, le damos un nombre a este paso en la interfaz del usuario. Luego, mediante la sección *inputs*, definimos los parámetros y configuraciones de esta tarea, que serán las siguientes:
```yaml
      command: 'build'
```
La tarea debe ejecutar el comando *build*, en el contexto de Docker, se va a construir una imagen de Docker a a partir de un *Dockerfile*.

```yaml
      Dockerfile: '**/Dockerfile'
```
Se específica la ubicación del archivo *Dockerfile* que se utilizará para construir la imagen de Docker. Tal como lo definimos, el sistema buscará el archivo *Dockerfile* en cualquier directorio dentro de la estructura del proyecto.
```yaml
      tags: 'latest'
```
Mediante esta línea específicamos la etiqueta que se aplicará a la imagen de Docker que se está construyendo, que será la versión más reciente de la imagen al indicar "*latest*".

Seguimos con la siguiente tarea:
```yaml
  - task: Docker@2
    displayName: 'Push Docker Image to Registry'
    inputs:
      command: 'push'
      tags: 'latest'
      containerRegistry: 'practicaVS'
```
Las tres primeras líneas serán exactamente iguales a la anterior tarea, en la primera línea se indica que usaremos la versión 2 de la tarea Docker, le damos un nombre a este paso y mediante *inputs* definimos los parámetros y configuraciones de la tarea, que será las siguientes:
```yaml
      command: 'push'
```
La tarea ejecutará el comando *push*, que en el contexto de Docker, es que se va "empujar" la imagen de Docker al registro de contenedores.

```yaml
      tags: 'latest'
```
Se vuelve a indicar que se utilizará la versión más reciente de la imagen, en este caso, la imagen que se "empujará" al registro.
```yaml
      containerRegistry: 'practicaVS'
```
Indicamos el nombre del registro de contenedores al que se enviará la imagen, en nuestro caso, "*practicaVS*".

Nos quedaría la última tarea:
```yaml
  - task: Docker@2
    displayName: 'Docker Compose Up'
    inputs:
      command: 'composeUp'
      dockerComposeFile: '**/docker-compose.yml'
      removeContainersOnPull: true
      detachedService: true
```
Las tres primeras línea son exactamente iguales a las tareas anteriores, en este caso, *inputs* está formado por lo siguiente:
```yaml
      command: 'composeUp'
```
La tarea ejecutará este comando, relacionado con la ejecución de **docker-compose up**.
```yaml
      dockerComposeFile: '**/docker-compose.yml'
```
Se indica la ubicación del archivo de configuración de Docker Compose que se utilizará. Se buscará el archivo de nombre **docker-compose.yml** en cualquier directorio dentro de la estructura del proyecto. 
```yaml
      removeContainersOnPull: true
```
Al darle el valor de verdadero, se eliminarán los contenedores existentes al realizar la operación de *pull*.
```yaml
      detachedService: true
```
Mediante esto, los servicios definidos en el archivo de Docker Compose, **docker-compose.yml**, se ejecutarán en segundo plano.
### azure-pipelines.yml - Práctica 2
```yaml
trigger:
- master

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UseDotNet@2
  inputs:
    packageType: 'sdk'
    version: '3.1.x'
    installationPath: $(Agent.ToolsDirectory)/dotnet

- script: |
    terraform init
    terraform validate
  displayName: 'Terraform Init and Validate'
  
- script: 'terraform plan -out=tfplan'
  displayName: 'Terraform Plan'
  
- script: 'terraform apply -auto-approve tfplan'
  displayName: 'Terraform Apply'
```
Nos encontramos con el segundo archivo requerido en la práctica, procedemos a desglosarlo:
```yaml
trigger:
- master

pool:
  vmImage: 'ubuntu-latest'
```
Al igual que en el archivo anterior, mediante la sección *trigger* definimos cuando debe ejecutarse el pipeline, en este caso, cuando se realicen cambios en la rama **master** del repositorio y mediante la sección *pool* definimos la máquina virtual en la que se van a ejecutar los pasos del *Pipeline*, que tambien usará la imagen "*ubuntu-latest*".

Tras esto, pasamos al bloque *steps*, donde definimos la secuencia de pasos que se ejecutarán en el *Pipeline*:
```yaml
steps:
- task: UseDotNet@2
  inputs:
    packageType: 'sdk'
    version: '3.1.x'
    installationPath: $(Agent.ToolsDirectory)/dotnet

- script: |
    terraform init
    terraform validate
  displayName: 'Terraform Init and Validate'
  
- script: 'terraform plan -out=tfplan'
  displayName: 'Terraform Plan'
  
- script: 'terraform apply -auto-approve tfplan'
  displayName: 'Terraform Apply'
```
Procedemos a dividirlo:
```yaml
- task: UseDotNet@2
  inputs:
    packageType: 'sdk'
    version: '3.1.x'
    installationPath: $(Agent.ToolsDirectory)/dotnet
```
En esta primera tarea usamos la versión 2 de la tarea UseDotNet y se realizará lo siguiente:
```yaml
    packageType: 'sdk'
```
Especificamos que se va a instalar el *Software Development Kit (SDK) de .NET*.
```yaml
    version: '3.1.x'
```
Concretamente la versión *3.1.x* de lo anterior.
```yaml
    installationPath: $(Agent.ToolsDirectory)/dotnet
```
Y se establece la ubicación donde se instalará el SDK de .NET en el agente de compilación.

Segunda bloque:
```yaml
- script: |
    terraform init
    terraform validate
  displayName: 'Terraform Init and Validate'
```
Ejecutamos un script que contiene dos comandos propios de *Terraform*, tal como vimos en la práctica anterior, con el primer comando inicializamos el directorio de trabajo de Terraform y mediante el segundo verificamos la sintaxis y validez de los archivos de configuración de Terraform. Tal como vimos anteriormente, mediante *displayName*, le damos un nombre a este paso en la interfaz del usuario.

Tercer bloque:
```yaml
- script: 'terraform plan -out=tfplan'
  displayName: 'Terraform Plan'
```
Ejecutamos el comando *terraform plan* que genera un plan de ejecución y mediante la opción *-out=tfplan* lo guardamos en un archivo llamado *tfplan*. Por último, lo volvemos a asignar un nombre a este paso que se mostrará en la intefaz de usuario.

Último bloque:
```yaml
- script: 'terraform apply -auto-approve tfplan'
  displayName: 'Terraform Apply'
```
Ejecutamos el comando indicado, el cual vimos también en la práctica anterior, mediante el que se aplicará los cambios en la infraestructura. Con la opción *-auto-approve* indicamos que Terraform no solicite confirmación antes de aplicar los cambios y por último, indicamos que el archivo de plan que se utilizará para aplicar los cambios sea *tfplan*. Volviéndole a asignar un nombre a este paso como último paso.

### Pipeline - GitLab
##### Stages
Primero se definen las diferentes etapas del pipeline, cada una con su propio conjunto de trabajos.
```yaml
stages:
  - clone
  - graph
  - upload
  - documentation
  - generate-html
```

##### Variables
Se definen algunas variables que se utilizan en el pipeline, como FIGSHARE_APP_ID, que se establece en el valor de la variable de entorno $figshare.
```yaml
variables:
  FIGSHARE_APP_ID: $figshare
```

##### Before Script
Contiene comandos que se ejecutan antes de cada trabajo en el pipeline. En este caso, se actualiza y se instala python3-venv en la máquina del corredor.
```yaml
before_script:
  - apt-get update -qy
  - apt-get install -y python3-venv
```

###### Clone Job
Este trabajo realiza la clonación del repositorio.
```yaml
clone-job:
  stage: clone
  script:
    - echo "Cloning the repository..."
    - git clone https://gitlab-ci-token:$CI_JOB_TOKEN@gitlab.com/$CI_PROJECT_PATH.git
    - cd practica_gitlab
```

###### Graph Job
Este trabajo genera gráficos utilizando un script Python llamado grafico.py y luego almacena la imagen generada como artefacto.
```yaml
graph-job:
  stage: graph
  script:
    - echo "Installing dependencies for graph job..."
    - apt-get install -y python3-venv
    - python3 -m venv venv
    - source venv/bin/activate || true
    - pip install pandas matplotlib
    - echo "Generating graphs..."
    - python3 grafico.py
    - echo "Graph generation complete."
  artifacts:
    paths:
      - grafica_sensor.png
```

###### Upload Job
Este trabajo instala dependencias, crea un entorno virtual y carga los gráficos generados a Figshare.
```yaml
  stage: upload
  script:
    - echo "Installing dependencies for upload job..."
    - apt-get install -y python3-venv
    - python3 -m venv venv
    - source venv/bin/activate || true
    - pip install figshare requests
    - echo "Uploading graphs to Figshare..."
    - cp grafica_sensor.png ./venv
    - python3 upload_to_figshare.py
    - echo "Graphs uploaded to Figshare successfully."
  dependencies:
    - graph-job
  artifacts:
    paths:
      - grafica_sensor.png
```

###### Documentation Job
Este trabajo genera documentación utilizando MkDocs y copia la imagen y el archivo README a la carpeta de documentos.
```yaml
documentation-job:
  stage: documentation
  script:
    - echo "Installing dependencies for documentation job..."
    - apt-get install -y python3-venv
    - python3 -m venv venv
    - source venv/bin/activate || true
    - pip install mkdocs
    - echo "Generating documentation..."
    - mkdocs new .
    - cp README.md docs/
    - cp grafica_sensor.png docs/
    - mkdocs build
    - echo "Documentation generation complete."
  dependencies:
    - graph-job
  artifacts:
    paths:
      - site/
      - grafica_sensor.png
```

###### Generate HTML Job
Este trabajo genera un artículo HTML a partir del README y embebe la imagen al final del archivo.
```yaml
generate-html-job:
  stage: generate-html
  script:
    - echo "Generating HTML article from README.md..."
    - apt-get install -y python3-venv
    - python3 -m venv venv
    - source venv/bin/activate || true
    - pip install grip
    - mkdir -p site
    - cp grafica_sensor.png site/
    - grip README.md --export site/index.html
    - echo "HTML article generation complete."
    - cat site/index.html
    - echo "Embedding image at the end of index.html..."
    - echo '<img src="grafica_sensor.png" alt="Graph" />' >> site/index.html
  dependencies:
    - documentation-job
  artifacts:
    paths:
      - site/index.html
      - site/grafica_sensor.png
```


Los script utilizados son sencillos, por ejemplo, el de la creación de la imágen png es el siguiente:
##### Script para Generar Gráficos desde Datos del Sensor

```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde CSV
df = pd.read_csv('SensorData.csv')

# Crear un gráfico de líneas para la temperatura y la humedad
plt.plot(df['timestamp'], df['temperatureSHT31'], label='Temperatura')
plt.plot(df['timestamp'], df['humiditySHT31'], label='Humedad')

# Configuraciones del gráfico
plt.title('Datos del Sensor')     # Título del gráfico
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()                      # Mostrar leyenda
plt.grid(True)                    # Mostrar cuadrícula en el gráfico

# Guardar el gráfico como imagen
plt.savefig('grafica_sensor.png')
```


El segundo script es el que se utiliza para subir el png a figshare, aquí está el código:
##### Script para Subir un Archivo a Figshare

###### Configuración Inicial
El script comienza importando las bibliotecas necesarias y configurando algunas variables, como el token de OAuth para la autorización.
```python
import os
import requests
import shutil

# Configurar token OAuth para autorización
oauth_token = '8b60245c20dfed8b906adde33d80c12eb8720e7b937ef4e29548785feb78a8087d0c9b81fe25a71b17640c25e934f21ef61af495815459f3c6b48827e28c529b'
```

###### Parámetros del Archivo a Subir
Se especifica la ruta del archivo PNG que se va a subir, así como el nombre y la descripción que se le asignarán en Figshare.
```python
# Ruta del archivo PNG que deseas subir
file_path = './venv/grafica_sensor.png'  # Cambiado para reflejar la ubicación correcta

# Nombre y descripción del artículo en Figshare
article_title = 'grafico.png'
article_description = 'Archivo de imagen'
```
###### URL de la API de Figshare
Se establece la URL de la API de Figshare para subir un archivo, así como se obtiene el tamaño del archivo.
```python
# URL de la API de Figshare para subir un archivo
upload_url = 'https://api.figshare.com/v2/account/articles/24926016/files'

# Obtener el tamaño del archivo
file_size = os.path.getsize(file_path)
```
###### Iniciar la Subida del Archivo
En esta sección, se realiza el primer paso para cargar un archivo en Figshare, que es iniciar la carga. Se utiliza una solicitud POST con el token OAuth y se proporcionan detalles sobre el archivo, como el nombre, la descripción y el tamaño.
```pyhon
try:
    initiate_response = requests.post(upload_url, headers={
        'Authorization': f'Bearer {oauth_token}',
        'Content-Type': 'application/json',
    }, json={
        'name': article_title,
        'description': article_description,
        'size': file_size
    })
    initiate_response.raise_for_status()
    initiate_data = initiate_response.json()
    upload_url = initiate_data.get('location')
    upload_token = initiate_data.get('upload_token')
except requests.exceptions.RequestException as e:
    print(f"Error al iniciar la carga del archivo: {e}")
    print(f"Detalles del error: {initiate_response.text}")
    exit(1)
```
###### Subir el Archivo
En esta sección, se realiza el segundo paso para cargar un archivo en Figshare, que es la subida real del archivo utilizando el URL de carga correcto obtenido en el paso anterior. Se utiliza una solicitud PUT con el token OAuth, el tipo de contenido y el token de carga.
```python
# Step 2: Upload the file using the correct upload URL
try:
    with open(file_path, 'rb') as file:
        response = requests.put(upload_url, headers={
            'Authorization': f'Bearer {oauth_token}',
            'Content-Type': 'application/octet-stream',
            'Content-Disposition': f'attachment; filename={article_title}',
            'Upload-Token': upload_token
        }, data=file.read())
        response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error al subir el archivo: {e}")
    exit(1)

print("Archivo subido exitosamente.")
```

Lo último que queda por explicar es el archivo de github pages, este se coloca en un workflow de la carpeta .github y en nuestro caso se llama pages.
```yaml
Este tiene un nombre y unas condiciones en las que se lanza, en nuestro caso cuando se actualiza la rama gh-pages
name: practica-gitlab

on:
  push:
    branches:
      - gh-pages
```

Contiene unos trabajos, que en nuestro caso es solo uno, el de despliegue que contiene varios pasos:
El primero es checkout, que clona el repositorio actual.
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
```
El segundo paso es descargar el artefacto generado en gitlab de la documentación.
```yaml

      - name: Download artifacts from GitLab
        run: |
          curl --location -o index.html "https://vs_uca_raulydavid.gitlab.io/-/practica_gitlab/-/jobs/5926421123/artifacts/site/index.html"
          ls -l    # Agregado para verificar si el archivo se descargó correctamente
          mkdir -p gh-pages
          cp index.html gh-pages/
```
Y como final tenemos el despliegue real de la página, utilizando un token de autenticación secreto del repositorio, para poder realizar un push.
```yaml
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.PAT_GITHUB }}
          publish_dir: ./gh-pages
          publish_branch: main
          force_orphan: true
          allow_empty_commit: true
```

# Practica Azure-GitLab
## Autores
> David Jesús Cerdeiro Gallardo

> Raul Ariza López
## Explicación de los ficheros y configuraciones
### azure-pipelines.yml - Práctica 1, Sección 3.4
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
### Pipeline - GitLab

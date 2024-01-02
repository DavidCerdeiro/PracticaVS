import os
import requests
from pprint import pprint

# Configure OAuth token for authorization
oauth_token = '52eae7844e5a73ad33b324d61131c76d4fbc1477ad6ec9813ea5c749845f2a6e7d5eb16bf28f650835fb560a8e10dcb5d9a863c6491caed5615b1736197e3a52'

# Ruta del archivo PNG que deseas subir
file_path = './grafica_sensor.png'

# Nombre y descripción del artículo en Figshare
article_title = 'Título de tu artículo en Figshare'
article_description = 'Descripción de tu artículo en Figshare'

# URL de la API de Figshare para subir un archivo
upload_url = 'https://api.figshare.com/v2/account/articles/24926016/files'
# Reemplaza '24926016' con el ID real de tu artículo

# Obtener el tamaño del archivo
file_size = os.path.getsize(file_path)

# Realizar la solicitud para obtener la URL de carga del archivo
try:
    response = requests.post(upload_url, headers={
        'Authorization': f'Bearer {oauth_token}',
        'Content-Type': 'application/json'
    }, json={
        'name': article_title,
        'description': article_description,
        'size': file_size
    })
    response.raise_for_status()
    upload_data = response.json()
    file_url = upload_data.get('upload_url')
except requests.exceptions.RequestException as e:
    print(f"Error al obtener la URL de carga: {e}")
    print(f"Detalles del error: {response.text}")
    exit(1)

# Subir el archivo al artículo usando la URL obtenida
try:
    with open(file_path, 'rb') as file:
        response = requests.put(file_url, headers={'Content-Type': 'application/octet-stream'}, data=file.read())
        response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error al subir el archivo: {e}")
    print(f"Detalles del error: {response.text}")
    exit(1)

print("Archivo subido exitosamente.")
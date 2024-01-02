import os
import requests
from pprint import pprint

# Configure OAuth token for authorization
oauth_token = '8b60245c20dfed8b906adde33d80c12eb8720e7b937ef4e29548785feb78a8087d0c9b81fe25a71b17640c25e934f21ef61af495815459f3c6b48827e28c529b'

# Ruta del archivo PNG que deseas subir
file_path = './grafica_sensor.png'

# Nombre y descripción del artículo en Figshare
article_title = 'grafico.py'
article_description = 'asas'

# URL de la API de Figshare para subir un archivo
upload_url = f'https://api.figshare.com/v2/account/articles/24926016/files'

# Obtener el tamaño del archivo
file_size = os.path.getsize(file_path)

# Realizar la solicitud para obtener la URL de carga del archivo y cargar el archivo en una sola conexión
try:
    with open(file_path, 'rb') as file:
        response = requests.post(upload_url, headers={
            'Authorization': f'Bearer {oauth_token}',
            'Content-Type': 'application/octet-stream',
            'Content-Disposition': f'attachment; filename={article_title}',
        }, params={
            'name': article_title,
            'description': article_description,
            'size': file_size
        }, data=file.read())
        response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error al subir el archivo: {e}")
    print(f"Detalles del error: {response.text}")
    exit(1)

print("Archivo subido exitosamente.")
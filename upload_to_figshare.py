import os
import requests
import json

def upload_to_figshare(file_path, figshare_token, article_id):
    # Configurar la URL de la API de Figshare para cargar archivos en un artículo específico
    upload_url = f'https://api.figshare.com/v2/account/articles/{article_id}/files'

    # Configurar el encabezado con el token de Figshare
    headers = {
        'Authorization': f'token {figshare_token}',
        'Content-Type': 'application/json',  # Especificar el tipo de contenido como JSON
    }

    # Crear el objeto de carga útil JSON con el campo "filedata"
    payload = {
        'filedata': (os.path.basename(file_path), open(file_path, 'rb')),
    }

    # Enviar la solicitud a Figshare
    response = requests.post(upload_url, headers=headers, files=payload)

    # Manejar la respuesta de Figshare
    if response.status_code == 201:
        print(f'Successfully uploaded {file_path} to Figshare!')
    else:
        print(f'Failed to upload {file_path} to Figshare. Status code: {response.status_code}')
        print(response.text)

# Configurar las variables necesarias
figshare_token = '64d223981d339c71a4a242888220713bbeb16509ddfbedc5eb6c50bd3b5b7da01d0b7a5faf9904d779ddbf19513e3bdc99a87e26a878531efc6956ad09fcb708'
article_id = '24926016'
file_path = './venv/grafica_sensor.png'

# Llamar a la función para subir el archivo
upload_to_figshare(file_path, figshare_token, article_id)
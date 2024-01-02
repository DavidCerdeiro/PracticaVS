from __future__ import print_function
import subprocess
import sys
from pprint import pprint

# Instalar las dependencias necesarias
subprocess.run(["pip", "install", "figshare"])

# Agregar la ruta del paquete figshare al sys.path
sys.path.append(sys.path[0] + '/venv/lib/python3.*/site-packages')

import swagger_client
from swagger_client.rest import ApiException

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Ruta del archivo PNG que deseas subir
file_path = 'path/to/your/file.png'

# Nombre y descripción del artículo en Figshare
article_title = 'Título de tu artículo en Figshare'
article_description = 'Descripción de tu artículo en Figshare'

# Crear instancia de la API
api_instance = swagger_client.FilesApi()

try:
    # Subir el archivo al artículo privado
    api_response = api_instance.private_file_create(file_path, title=article_title, description=article_description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->privateFileCreate: %s\n" % e)
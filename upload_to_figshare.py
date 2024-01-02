import os
from figshare.api import FilesApi
from figshare.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
os.environ['FIGSHARE_API_KEY'] = '52eae7844e5a73ad33b324d61131c76d4fbc1477ad6ec9813ea5c749845f2a6e7d5eb16bf28f650835fb560a8e10dcb5d9a863c6491caed5615b1736197e3a52'

# Ruta del archivo PNG que deseas subir
file_path = './grafica_sensor.png'

# Nombre y descripción del artículo en Figshare
article_title = 'Título de tu artículo en Figshare'
article_description = 'Descripción de tu artículo en Figshare'

# Crear instancia de la API
api_instance = FilesApi()

try:
    # Subir el archivo al artículo privado
    api_response = api_instance.private_file_create(file_path, title=article_title, description=article_description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->privateFileCreate: %s\n" % e)
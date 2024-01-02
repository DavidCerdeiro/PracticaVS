import swagger_client
from swagger_client.rest import ApiException

# Configurar OAuth2 access token para la autorización: OAuth2
swagger_client.configuration.access_token = '64d223981d339c71a4a242888220713bbeb16509ddfbedc5eb6c50bd3b5b7da01d0b7a5faf9904d779ddbf19513e3bdc99a87e26a878531efc6956ad09fcb708'

# Crear una instancia de la clase de la API
api_instance = swagger_client.ArticlesApi()

# ID único del artículo
article_id = 789

# Ruta del archivo PNG que quieres subir
file_path = './grafica_sensor.png'

try:
    # Configurar el objeto de carga de archivo
    file_payload = swagger_client.FileUploadDto(file_path=file_path)

    # Llamada para crear un nuevo archivo en el artículo
    api_response = api_instance.create_file(article_id, file_payload)
    print(api_response)
except ApiException as e:
    print("Excepción al llamar a ArticlesApi->create_file: %s\n" % e)
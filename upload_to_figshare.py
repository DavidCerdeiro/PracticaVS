import figshare
import requests

def upload_image(api_token, file_path):
    # Utiliza APIClient en lugar de Figshare
    client = figshare.APIClient(api_token=api_token)

    # Carga el archivo en Figshare
    article = client.file_upload(file_path)

    # Imprime el enlace al artículo creado
    print("File uploaded successfully. Article URL:", article['location'])

# Llama a la función de carga de imágenes
upload_image(api_token="64d223981d339c71a4a242888220713bbeb16509ddfbedc5eb6c50bd3b5b7da01d0b7a5faf9904d779ddbf19513e3bdc99a87e26a878531efc6956ad09fcb708", file_path="./venv/grafica_sensor.png")
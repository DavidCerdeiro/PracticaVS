# Contenido de upload_to_figshare.py

import figshare

def upload_image(api_token, file_path):
    # Configurar el cliente Figshare
    client = figshare.Figshare(api_token=api_token)

    # Crear un nuevo artículo en Figshare
    article = client.create_article(title="Graph Image", description="Uploaded from GitLab CI")

    # Subir la imagen al artículo
    file_id = client.upload_file_to_article(article_id=article['id'], file_path=file_path)

    print(f"Image uploaded to Figshare with file ID: {file_id}")

# Usar la función con el token de la API de Figshare y la ruta de la imagen
upload_image(api_token="64d223981d339c71a4a242888220713bbeb16509ddfbedc5eb6c50bd3b5b7da01d0b7a5faf9904d779ddbf19513e3bdc99a87e26a878531efc6956ad09fcb708", file_path="./venv/grafica_sensor.png")
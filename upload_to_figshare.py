import os
import sys

# Agregar el directorio figshare_api al path para importar Figshare
sys.path.append(os.path.join(os.path.dirname(__file__), "venv/lib/python3.*/site-packages"))

from figshare.figshare_api import Figshare

def upload_to_figshare(api_key, file_path, article_title, article_description):
    # Configurar la conexión a Figshare
    figshare = Figshare(api_key=api_key)

    # Crear un nuevo artículo en Figshare
    article = figshare.create_article(title=article_title, description=article_description)

    # Subir el archivo al artículo
    article.add_file(file_path)

if __name__ == "__main__":
    # Definir las variables necesarias
    api_key = os.environ.get("FIGSHARE_APP_ID")
    file_path = "venv/grafica_sensor.png"  # Asegúrate de que la ruta sea correcta
    article_title = "Título del Artículo en Figshare"
    article_description = "Descripción del Artículo en Figshare"

    # Llamar a la función para subir a Figshare
    upload_to_figshare(api_key, file_path, article_title, article_description)
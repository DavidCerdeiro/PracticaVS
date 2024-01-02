import os
from figshare.api import Figshare
from figshare.figshare_article import FigshareArticle

def upload_to_figshare(api_key, file_path, article_title, article_description):
    # Configurar la conexión a Figshare
    figshare = Figshare(api_key=api_key)

    # Crear un nuevo artículo en Figshare
    article = FigshareArticle(figshare)
    article.title = article_title
    article.description = article_description
    article.add_file(file_path)

    # Guardar el artículo en Figshare
    article.save()

if __name__ == "__main__":
    # Definir las variables necesarias
    api_key = os.environ.get("FIGSHARE_APP_ID")
    file_path = "venv/grafica_sensor.png"  # Asegúrate de que la ruta sea correcta
    article_title = "Título del Artículo en Figshare"
    article_description = "Descripción del Artículo en Figshare"

    # Llamar a la función para subir a Figshare
    upload_to_figshare(api_key, file_path, article_title, article_description)
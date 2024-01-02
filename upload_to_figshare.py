import figshare

def upload_image(api_token, file_path):
    # Create an authenticated session
    auth = figshare.FigshareAuth(api_token=api_token)
    session = figshare.FigshareSession(auth)

    # Create a new article (data structure to store your files)
    article = session.create_article(title="My Graph Article", defined_type="dataset")

    # Upload the file to the article
    article.upload_file(file_path)

    # Save the article
    article.save()

    # Publish the article (make it publicly accessible)
    article.publish()

if __name__ == "__main__":
    # Replace 'your_api_token' with your actual Figshare API token
    upload_image(api_token="64d223981d339c71a4a242888220713bbeb16509ddfbedc5eb6c50bd3b5b7da01d0b7a5faf9904d779ddbf19513e3bdc99a87e26a878531efc6956ad09fcb708",
                 file_path="./venv/grafica_sensor.png")
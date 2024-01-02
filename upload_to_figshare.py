import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = '8b60245c20dfed8b906adde33d80c12eb8720e7b937ef4e29548785feb78a8087d0c9b81fe25a71b17640c25e934f21ef61af495815459f3c6b48827e28c529b'

# create an instance of the API class
api_instance = swagger_client.ArticlesApi()
articleId = 24926016  # Long | Article unique identifier
file = './grafica_sensor.png'

try:
    # Initiate Upload
    api_response = api_instance.private_article_upload_initiate(articleId, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->privateArticleUploadInitiate: %s\n" % e)
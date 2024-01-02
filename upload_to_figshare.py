#!/usr/bin/env python

import hashlib
import os
import requests
from requests.exceptions import HTTPError

BASE_URL = 'https://api.figshare.com/v2/{endpoint}'
TOKEN = '52eae7844e5a73ad33b324d61131c76d4fbc1477ad6ec9813ea5c749845f2a6e7d5eb16bf28f650835fb560a8e10dcb5d9a863c6491caed5615b1736197e3a52'
CHUNK_SIZE = 1048576

FILE_PATH = './grafica_sensor.png'
ARTICLE_TITLE = 'My Article Title'


def raw_issue_request(method, url, data=None, binary=False, files=None):
    headers = {'Authorization': 'token ' + TOKEN}
    if data is not None and not binary:
        response = requests.post(url, headers=headers, json=data, files=files)
    else:
        response = requests.request(method, url, headers=headers, data=data)
    
    try:
        response.raise_for_status()
        try:
            data = response.json()
        except ValueError:
            data = response.content
    except HTTPError as error:
        print('Caught an HTTPError: {}'.format(error))
        print('Body:\n', response.content)
        raise

    return data


def issue_request(method, endpoint, *args, **kwargs):
    return raw_issue_request(method, BASE_URL.format(endpoint=endpoint), *args, **kwargs)


def list_articles():
    result = issue_request('GET', 'account/articles')
    print('Listing current articles:')
    if result:
        for item in result:
            print(u'  {url} - {title}'.format(**item))
    else:
        print('  No articles.')
    print()


def create_article(title):
    data = {
        'title': title
    }
    result = issue_request('POST', 'account/articles', data=data)
    print('Created article:', result['location'], '\n')

    result = raw_issue_request('GET', result['location'])

    return result['id']


def list_files_of_article(article_id):
    result = issue_request('GET', 'account/articles/{}/files'.format(article_id))
    print('Listing files for article {}:'.format(article_id))
    if result:
        for item in result:
            print('  {id} - {name}'.format(**item))
    else:
        print('  No files.')

    print()


def get_file_check_data(file_name):
    with open(file_name, 'rb') as fin:
        md5 = hashlib.md5()
        size = 0
        data = fin.read(CHUNK_SIZE)
        while data:
            size += len(data)
            md5.update(data)
            data = fin.read(CHUNK_SIZE)
        return md5.hexdigest(), size


def initiate_new_upload(article_id, file_name):
    endpoint = 'account/articles/{}/files'
    endpoint = endpoint.format(article_id)

    md5, size = get_file_check_data(file_name)
    data = {
        'name': os.path.basename(file_name),
        'md5': md5,
        'size': size,
    }

    with open(file_name, 'rb') as fin:
        files = {'file': (os.path.basename(file_name), fin)}
        result = issue_request('POST', endpoint, data=data, files=files)

    print('Initiated file upload:', result['location'], '\n')

    result = raw_issue_request('GET', result['location'])

    return result


def complete_upload(article_id, file_id):
    issue_request('POST', 'account/articles/{}/files/{}'.format(article_id, file_id))


def upload_file(file_path):
    list_articles()
    article_id = create_article(ARTICLE_TITLE)
    list_articles()
    list_files_of_article(article_id)

    file_info = initiate_new_upload(article_id, file_path)
    list_files_of_article(article_id)

if __name__ == '__main__':
    upload_file(FILE_PATH)
import json


def get_authentication(credentials_file):
    with open(credentials_file, 'r') as file:
        credentials_data = json.load(file)

    api_key = credentials_data['APIkey']
    url = credentials_data['URL']

    file.close()

    return url, api_key

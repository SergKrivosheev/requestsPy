import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path: str, name):
        href = self._get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

if __name__ == '__main__':
    path_to_file =r'C:\Users\Кривошеев\PycharmProjects\requestsPy\Upload.txt'
    with open('YaToken.txt', 'r') as f:
        token = f.read()
    uploader = YaUploader(token)
    #pprint(uploader.get_files_list())
    result = uploader.upload("netology/Upload.txt", "Upload.txt" )
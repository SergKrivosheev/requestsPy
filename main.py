import requests
from pprint import pprint
#from ya_disk import YandexDisk

TOKEN = "AQAAAAAdpZo9AADLW_BPQnS3WkjlpgGLsCNU03E"

def test_requests():
    url = "https://httpbin.org/get"
    params = {"color": "615"}
    headers = {"Autorization": "secret - token - 123", "My_header":"my_header_value"}
    response = requests.get(url=url, params=params, headers=headers)
    pprint(response.content)

if __name__ == '__main__':
    test_requests()

    #ya = YandexDisk(token=TOKEN)
    #pprint(ya.get_files_list())
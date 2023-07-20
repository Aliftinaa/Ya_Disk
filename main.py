import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
                }

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        params = {'path': 'test.txt-', 'overwrite': True}
        resp = requests.get(url, headers=self.get_headers(), params=params).json()
        upload_link = resp.get('href')
        response = requests.put(upload_link, data=open(path_to_file, 'rb'), headers=self.get_headers())
        print(response.status_code)


if __name__ == '__main__':
    path_to_file = r'C:\Users\admin\PycharmProjects\pythonProject6\test.txt'
    token = 'y0_AgAAAABvf9EXAADLWwAAAADoOHP7oL5tH89_RCW_QFv8WlOgSuq09lI'
    uploader = YaUploader(token)
    uploader.upload(path_to_file)




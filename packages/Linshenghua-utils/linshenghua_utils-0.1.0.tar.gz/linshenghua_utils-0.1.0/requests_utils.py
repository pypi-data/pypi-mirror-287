# requests 类封装操作
import requests


class RequestsUtils:
    def __init__(self, headers=None):
        self.headers = headers

    def get(self, url, params=None):
        response = requests.get(url, params=params, headers=self.headers)
        return response

    def post(self, url, data=None, json=None):
        response = requests.post(url, data=data, json=json, headers=self.headers)
        return response

    def delete(self, url, params=None):
        response = requests.delete(url, params=params, headers=self.headers)
        return response

    def send_req(self, method, **kwargs):
        if method.lower() == 'get':
            response = self.get(**kwargs)
        elif method.lower() == 'post':
            response = self.post(**kwargs)
        elif method.lower() == 'delete':
            response = self.delete(**kwargs)
        else:
            raise ValueError('Unsupported HTTP method')
        return response


req = RequestsUtils()

# 示例用法
if __name__ == '__main__':
    # 示例用法
    url1 = 'https://www.baidu.com'
    req = RequestsUtils()
    # 发起GET请求
    response1 = req.get(url1)
    print(response1.status_code)

    response2 = req.send_req('get', url=url1)
    print(response2.status_code)

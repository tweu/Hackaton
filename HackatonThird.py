import requests
from requests.api import request
from requests.sessions import Request

response = requests.get('http://206.189.44.36:8900/students/')
result = response.json()


for i in result:
    if response.status_code == 204:
        print('Успешно удалено!')
    else:
        print('Всё правильно :) ', response.status_code)


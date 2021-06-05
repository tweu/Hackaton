import requests
from requests.api import request

student =       {
        "id": 8,
        "name": "HackatonStudent1",
        "age": 123,
        "group": "Python-23",
        "phone": "+996438874774",
        "email": "HelloThere@gmail.com",
        "date_joined": "2021-05-28T17:45:42.211688+06:00",
        "updated": "2021-05-28T17:45:42.211712+06:00",
        "created_by": "Команда: 1"
    }

response = requests.post('http://206.189.44.36:8900/students/', data = student)
result = response.json()

import requests

response = requests.get('http://206.189.44.36:8900/students/9/') #В первом файле создалось два новых студента и самый первый id нового студента это 9
result = response.json()
result2 =(result["name"], result["age"], result["group"])
for i in enumerate(result2, start=1):
    print(i)
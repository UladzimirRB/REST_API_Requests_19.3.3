import requests
import json

status = 'available'
response = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})

response_status = response.status_code
print("*******************************************************")
print(f"Статус ответа от сервера на GET запрос: {response_status}")

try:
    result = response.json()
except:
    result = response.text

print(result)

#=====================================================
''' POST запрос '''

info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Dandy",
  "photoUrls": [
    "Dandy's photo"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                         data=json.dumps(info, ensure_ascii=False))
response_status = response.status_code
print("*******************************************************")
print(f"Статус ответа от сервера на POST запрос: {response_status}")

try:
    result = response.json()
except:
    result = response.text

print(result)
print(f"ID number добавленного питомца = {result['id']}")
print(f"Имя добавленного питомца = {result['name']}")
print("************************************************************")
#=======================================================================

info = {
  "id": result['id'],
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Milka",
  "photoUrls": [
    "Milka's photo"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response = requests.put(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                         data=json.dumps(info, ensure_ascii=False))
response_status = response.status_code
print(f"Статус ответа от сервера на PUT запрос: {response_status}")

try:
    result = response.json()
except:
    result = response.text

print(result)
print(f"ID number питомца данные которого изменяются = {result['id']}")
print(f"Новое имя питомца = {result['name']}")
print("************************************************************")

#====================================================================

response = requests.delete(f"https://petstore.swagger.io/v2/pet/{result['id']}", headers = {'accept': 'application/json'})

response_status = response.status_code
print(f"Статус ответа от сервера на DELETE запрос: {response_status}")

try:
    result = response.json()
except:
    result = response.text

print(result)
print("************************************************************")

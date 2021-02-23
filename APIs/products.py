import requests
import json

response = requests.get('https://hplussport.com/api/products')
print(response)
print(type(response))
content = response.content
json_content = json.loads(content)
print(json_content)
print(type(json_content))
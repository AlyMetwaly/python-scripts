import requests
import json

url = "https://easy-instagramapi.p.rapidapi.com/v1/profile/nasa/media"

headers = {
    'x-rapidapi-key': "ff7ce49e53msh68338a7077a8c62p14160bjsnf20ebcef7e02",
    'x-rapidapi-host': "easy-instagramapi.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
#print(response.text)
content = response.content
json_content = json.loads(content)
items = json_content['items']
first_item = items[0]
print(first_item)

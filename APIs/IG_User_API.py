import requests
import json
from datetime import date

url = "https://easy-instagramapi.p.rapidapi.com/v1/profile/alymyoussef"

headers = {
    'x-rapidapi-key': "ff7ce49e53msh68338a7077a8c62p14160bjsnf20ebcef7e02",
    'x-rapidapi-host': "easy-instagramapi.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
print(response.text)
content = response.content
json_content = json.loads(content)
#print(json_content)
followers_Count = json_content['followersCount']
#print(type.json_content)
#print('Date:',date.today(),'Followers Count:',followersCount) >> f
with open('Aly Metwaly.txt', 'a') as f:
  print('Date:',date.today(),'Followers Count:',followers_Count, file=f)
f.close()

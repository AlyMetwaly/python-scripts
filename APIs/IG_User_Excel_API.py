import requests
import json
from datetime import date
import pandas as pd

url = "https://easy-instagramapi.p.rapidapi.com/v1/profile/alymyoussef"

headers = {
    'x-rapidapi-key': "ff7ce49e53msh68338a7077a8c62p14160bjsnf20ebcef7e02",
    'x-rapidapi-host': "easy-instagramapi.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
#print(response.text)
content = response.content
json_content = json.loads(content)
followersCount = json_content['followersCount']
todayDate = date.today()
df = pd.DataFrame({'Date':todayDate,'FollowersCount':followersCount})
df.to_excel('./aly_metwaly.xlsx')

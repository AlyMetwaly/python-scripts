import requests

url = "https://easy-instagramapi.p.rapidapi.com/v1/profile/nasa"

headers = {
    'x-rapidapi-key': "ff7ce49e53msh68338a7077a8c62p14160bjsnf20ebcef7e02",
    'x-rapidapi-host': "easy-instagramapi.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
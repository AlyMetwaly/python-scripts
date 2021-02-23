import requests

url = "https://linkedin2email.p.rapidapi.com/in/aly-metwaly"

headers = {
    'x-rapidapi-key': "ff7ce49e53msh68338a7077a8c62p14160bjsnf20ebcef7e02",
    'x-rapidapi-host': "linkedin2email.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
import requests

url = "https://instagram-profile-picture1.p.rapidapi.com/api/v1/profile/data"

querystring = {"username":"alymyoussef"}

headers = {
    'x-rapidapi-key': "ff7ce49e53msh68338a7077a8c62p14160bjsnf20ebcef7e02",
    'x-rapidapi-host': "instagram-profile-picture1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
import requests
import json


print('PHOTO DOWNLOADING ------------------')

def __init__(self, url):
    self.url = url

def in_json(self):
    d = {
    'url': self.url,
        }
    return d

def __repr__(self):
    return self.url

with open("json.json", "r") as file:
    in_json_ = json.load(file)

for data in in_json_["data"]:
    response = requests.get(data["url"])
   
with open("photo.jpeg", 'wb') as file:
    file.write(response.content)


print("PHOTO DOWNLOADED ----------")



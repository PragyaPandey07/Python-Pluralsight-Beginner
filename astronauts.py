import requests

response = requests.get('http://api.open-notify.org/astros.json')
json_res = response.json()

for astronaut in json_res['people']:
    print(astronaut['name'], astronaut['craft']) 
import requests

city = 'Bangalore'
req_url = 'https://api.weatherapi.com/v1/current.json?key=252cd6d6c6f24cb58b572116240304&q='+city+'&aqi=no'
response = requests.get(req_url)
weather_res = response.json()

temperature = weather_res.get('current').get('temp_c')
condition = weather_res.get('current').get('condition').get('text')

print('The temperature of',city, 'is',temperature,'and weather is', condition) 
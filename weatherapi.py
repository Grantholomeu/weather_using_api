import requests

API_KEY = "5713d4aab87b3cd93b9643dc197b737e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter the name of a city: ")

#This constructs the url we want to hit using the variables defined earlier and from the input.
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

#This retrieves the data from the api corresponding to our inputted city. 
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print('Weather: ', weather)
    temperature = round(data['main']['temp'] - 273.15, 2)
    print('Temperature: ', temperature, 'Celsius')

else: 
    print("An error has occured")

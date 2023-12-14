
import requests

api_key = '55aae6de3718fd1bcad31bd28e40ddeb'


user_input = input("enter city: ")

 

weather_data = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {temp}ºF")




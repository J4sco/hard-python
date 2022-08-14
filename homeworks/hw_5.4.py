import datetime
import json
import requests

# restituisce l'ora attuale come stringa (12, 15, ...)
hours = int(datetime.datetime.now().strftime("%H"))

with open('lezione5/data/province.json', 'r') as f:
  provinces = json.load(f)

#provinces è una dizionario: per ottenere lat e lon:
    # provinces["Agrigento"] restituisce "{'lat': '37.18', 'lon': '13.36'}"  (str)
    # provinces["Agrigento"]["lat"] restitusce "37.18"   (str)

## loop for human interaction ##
isNotValid = True
location = input("Insert the province that you want to check: ")
while isNotValid:
    try:
        if location not in provinces:
            raise Exception("Invalid name, try again.")
        else: isNotValid = False
    except Exception as ex:
        print(ex)
        location = input("Insert the province that you want to check: ")

latitude = provinces[location]["lat"]
longitude = provinces[location]["lon"]

url= "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m,apparent_temperature&timezone=Europe/Rome".format(latitude, longitude)
weather = requests.get(url).json()

temperature = weather["hourly"]["temperature_2m"][hours]
apparent_t = weather["hourly"]["apparent_temperature"][hours]
    
print("--> The temperature in {} is {} °C ({} °C apparent)".format(location, temperature, apparent_t))

# save the results as a log 
with open('homeworks/weather.json', 'w') as file:
    json.dump(weather, file, indent=3)
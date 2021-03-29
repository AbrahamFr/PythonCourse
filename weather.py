import requests

def get_weather_desc_and_temp():
    api_key = 'e2205d13dbc7c98a2d6a99c3cff1addd'
    city = "Orlando"
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key+'&units=imperial'

    request = requests.get(url)
    json = request.json()
    #print(json)

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {
        'description': description,
        'temp_min': temp_min,
        'temp_max': temp_max   
    }

def main():
    # Print the results
    weather_dict = get_weather_desc_and_temp()
    print("Today's forecast is", weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'))
    print("The maximum temperature is", weather_dict.get('temp_max'))

main()

# temperature =50
# forecast = "rain"
# raining = True
# if raining:
#     print("Stay inside!")


# if temperature < 80 or forecast != "reain":
#     print("Go outside!")
# else: 
#     print("Stay inside!")


# if temperature > 80:
#     print("It's too hot!")
#     print("Stay inside!")
# elif temperature < 60:
#     print("It's too cold!")
#     print("Stay inside!")
# else:
#     print("Enjoy the outdoors")
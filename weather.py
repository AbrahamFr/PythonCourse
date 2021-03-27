import requests

api_key = 'e2205d13dbc7c98a2d6a99c3cff1addd'
city = "Orlando"
url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key+'&units=imperial'

request = requests.get(url)
json = request.json()
print(json)

description = json.get("weather")[0].get("description")
print("Today's forecast is", description)



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
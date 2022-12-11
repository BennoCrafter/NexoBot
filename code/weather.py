import requests
import PrivateConfigs


class GetWeather:
    API_key = PrivateConfigs.weather_api_key

    lon = PrivateConfigs.lon
    lat = PrivateConfigs.lat

    request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    response = requests.get(request_url)

    if response.status_code == 200:
        print("Logged Sucsesfully!")
        data = response.json()
        weather_description = data["weather"][0]["description"]
        tempreature = round(data["main"]["temp"]-273.15)
        print("Das Wetter ist " + weather_description)
        print("Die Temperatur beträgt " + str(tempreature) + " Grad Celcius")
    else:
        print("Ich konnte keine Daten auslesen!")
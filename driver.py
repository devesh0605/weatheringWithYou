def forcaster(citnam):
    import requests

    api_key = "6af44f0c54d0eb4dd6a074d3010ea71b"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = citnam

    complete_url = base_url + "q=" + city_name + "&appid=" + api_key

    response = requests.get(complete_url)

    a = response.json()

    return a



import requests
def temp(zip_code, country):
    api_key = '6191e2e44347bbac151178edc76e5481'
    country_code = {value.lower():key.lower() for key, value in requests.get("http://country.io/names.json").json().items()}[country.lower()]
    kelvin = requests.get(f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}").json()['main']['temp']
    fahrenheit = round((kelvin - 273.15) * 9/5 + 32, 1)
    return fahrenheit
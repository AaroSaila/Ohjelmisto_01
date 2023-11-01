import requests

api_key = "404f93a3ca1a1e108fa623b09646cb76"


def main():
    city = input("Hea kaupungin säätä: ")
    search = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=fi&units=metric"
    try:
        result = requests.get(search)
        if result.status_code == 200:
            json_result = result.json()
            weather = json_result["weather"][0]["description"]
            temperature = json_result["main"]["temp"]
            print(f"Säätila ja lämpötila kaupungissa {city.capitalize()}: {weather}, {temperature} C")
        elif result.status_code == 404:
            print("Kaupunkia ei löytynyt")
    except requests.exceptions.RequestException:
        print("ERROR")


main()

import requests


def main():
    try:
        joke = requests.get("https://api.chucknorris.io/jokes/random")
        if joke.status_code == 200:
            json_joke = joke.json()
            print(json_joke["value"])

    except requests.exceptions.RequestException:
        print("ERROR")


main()

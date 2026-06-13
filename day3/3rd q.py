import requests


def get_random_joke() -> None:
    url: str = "https://official-joke-api.appspot.com/random_joke"

    response: requests.Response = requests.get(url)

    if response.status_code == 200:
        joke: dict = response.json()

        print("😂 Random Joke")
        print("-" * 30)
        print(f"Setup: {joke['setup']}")
        print(f"Punchline: {joke['punchline']}")
    else:
        print(f"Error: {response.status_code}")


def main() -> None:
    get_random_joke()


main()
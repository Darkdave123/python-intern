import requests


def fetch_user(username: str) -> dict:
    """
    Fetch GitHub user data from the GitHub API.
    """
    url: str = f"https://api.github.com/users/{username}"

    try:
        response: requests.Response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: User '{username}' not found.")
            return {}

    except requests.exceptions.RequestException:
        print("Network error: Unable to connect to GitHub API.")
        return {}


def fetch_joke() -> tuple[str, str]:
    """
    Fetch a random joke from the Joke API.
    """
    url: str = "https://official-joke-api.appspot.com/random_joke"

    try:
        response: requests.Response = requests.get(url, timeout=10)

        if response.status_code == 200:
            joke: dict = response.json()

            setup: str = joke.get("setup", "No setup available")
            punchline: str = joke.get("punchline", "No punchline available")

            return setup, punchline

        print("Error: Unable to fetch joke.")
        return "", ""

    except requests.exceptions.RequestException:
        print("Network error: Unable to connect to Joke API.")
        return "", ""


def display_user(user: dict) -> None:
    """
    Display GitHub user information in a formatted card.
    """
    if not user:
        print("No user data available.")
        return

    print("\n===== GitHub User Card =====")
    print(f"Name         : {user.get('name')}")
    print(f"Username     : {user.get('login')}")
    print(f"Location     : {user.get('location')}")
    print(f"Public Repos : {user.get('public_repos')}")
    print(f"Created At   : {user.get('created_at')}")
    print("============================")


def main() -> None:
    username: str = input("Enter GitHub username: ")

    user: dict = fetch_user(username)
    display_user(user)

    setup, punchline = fetch_joke()

    if setup and punchline:
        print("\n===== Random Joke =====")
        print(f"Setup     : {setup}")
        print(f"Punchline : {punchline}")


main()
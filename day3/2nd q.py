import requests


def get_github_user(username: str) -> None: 
    url: str = f" https://api.github.com/users/octocat"

    response: requests.Response = requests.get(url)

    if response.status_code == 200:
        data: dict = response.json()

        print("\nGitHub User Details")
        print("-" * 30)
        print(f"Name         : {data['name']}")
        print(f"Location     : {data['location']}")
        print(f"Public Repos : {data['public_repos']}")
        print(f"Created At   : {data['created_at']}")
    else:
        print(f"Error: Unable to fetch data (Status Code: {response.status_code})")


def main() -> None:
    get_github_user("octocat")


main()
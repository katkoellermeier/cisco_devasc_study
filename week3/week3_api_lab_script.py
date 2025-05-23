
# Week 3 Lab: REST API + JSON Parsing
# Author: [Kat Koellermeier]
# Purpose: Make a GET request to a public API and parse the JSON response

import requests

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print(f"Name: {user_data.get('name')}")
        print(f"Public Repos: {user_data.get('public_repos')}")
        print(f"Followers: {user_data.get('followers')}")
        print(f"Bio: {user_data.get('bio')}")
    else:
        print(f"Failed to retrieve data for user {username} (Status Code: {response.status_code})")

if __name__ == "__main__":
    username = input("Enter a GitHub username: ").strip()
    get_github_user_info(username)

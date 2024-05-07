#!/usr/bin/python3
"""Function to display popular posts on a specified Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Display the titles of the 10 most popular posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "redditdev scraper by u/bikaze"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()  # Raise an exception
        results = response.json().get("data")
        if not results:
            print("None")
            return
        [print(c.get("data").get("title")) for c in results.get("children")]
    except requests.exceptions.RequestException as e:
        # Handle various exceptions that can occur during the request
        print(None)

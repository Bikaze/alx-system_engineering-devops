#!/usr/bin/python3
"""This is a function that gets the number of subscribers on a given
Subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "redditdev scraper by u/bikaze"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception
        results = response.json().get("data")
        if not results:
            return 0
        return results.get("subscribers")
    except requests.exceptions.RequestException as e:
        # Handle various exceptions that can occur during the request
        return 0

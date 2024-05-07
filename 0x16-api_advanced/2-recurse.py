#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves the titles of all hot posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve posts from.
        hot_list (list, optional): The list to store the post titles.
        Defaults to an empty list.
        after (str, optional): The "after" parameter for pagination.
        Defaults to an empty string.
        count (int, optional): The current count of retrieved posts.
        Defaults to 0.

    Returns:
        list: A list of the titles of all hot posts on the given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "redditdev scraper by u/bikaze"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()  # Raise an exception
        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for post in results.get("children"):
            hot_list.append(post.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    except requests.exceptions.RequestException as error:
        return None

#!/usr/bin/python3
"""This script using a REST API, for a given employee ID, returns
information about his/her TODO list progress."""

if __name__ == '__main__':
    import requests
    import sys

    user_id = sys.argv[1]
    endpoint = "https://jsonplaceholder.typicode.com/users"
    nm = requests.get(url=f"{endpoint}/{user_id}").json()['username']
    dt_todo = requests.get(url=f"{endpoint}/{user_id}/todos").json()
    tasks = [(x['title'], x['completed']) for x in dt_todo]
    with open(f"{user_id}.csv", "w") as f:
        for task, status in tasks:
            f.write(f'"{user_id}","{nm}","{status}","{task}"\n')

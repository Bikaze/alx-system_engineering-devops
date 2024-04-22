#!/usr/bin/python3
"""This script using a REST API, for a given employee ID, returns
information about his/her TODO list progress."""

if __name__ == '__main__':
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    endpoint = "https://jsonplaceholder.typicode.com/users"
    nm = requests.get(url=f"{endpoint}/{user_id}").json()['username']
    dt_todo = requests.get(url=f"{endpoint}/{user_id}/todos").json()
    rm_keys = ['userId', 'id']
    tasks = [{key: value for key, value in x.items() if key not in rm_keys}
             for x in dt_todo]
    for i in tasks:
        i['task'] = i.pop('title')
        i['username'] = nm
    data = {f"{user_id}": tasks}
    with open(f"{user_id}.json", "w") as f:
        json.dump(data, f)

#!/usr/bin/python3
"""This script using a REST API, for a given employee ID, returns
information about his/her TODO list progress."""

if __name__ == '__main__':
    import json
    import requests
    import sys

    def format_user(info):
        user_id = info[0]
        endpoint = "https://jsonplaceholder.typicode.com/users"
        nm = info[1]
        dt_todo = requests.get(url=f"{endpoint}/{user_id}/todos").json()
        rm_keys = ['userId', 'id']
        tasks = [{key: value for key, value in x.items() if key not in rm_keys}
                 for x in dt_todo]
        for i in tasks:
            i['task'] = i.pop('title')
            i['username'] = nm
        data = {f"{user_id}": tasks}
        return data

    usr = requests.get(url="https://jsonplaceholder.typicode.com/users").json()
    usr = [(x['id'], x['username']) for x in usr]
    data = {}
    for i in usr:
        data.update(format_user(i))
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)

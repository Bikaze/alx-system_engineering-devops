#!/usr/bin/python3
"""This script using a REST API, for a given employee ID, returns
information about his/her TODO list progress."""

import requests
import sys

user_id = sys.argv[1]
endpoint = "https://jsonplaceholder.typicode.com/users"
nm = requests.get(url=f"{endpoint}/{user_id}").json()['name']
data_todo = requests.get(url=f"{endpoint}/{user_id}/todos").json()
cmpltd_tsks = [x['title'] for x in data_todo if x['completed'] is True]
l1 = f"Employee {nm} is done with tasks({len(cmpltd_tsks)}/{len(data_todo)}):"
print(l1)
for i in cmpltd_tsks:
    print('\t', i)

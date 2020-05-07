#!/usr/bin/python3
"""
get data from an api based on the userd id that is passed as argument
"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/users/'

    persons_res = requests.get(url)
    person_obj = persons_res.json()

    """ working with the data """
    total = {}

    for user in person_obj:
        _id = user['id']
        result = []
        res = requests.get('{}{}/todos'.format(url, _id)).json()

        for obj in res:
            task = {}
            task['task'] = obj['title']
            task['completed'] = obj['completed']
            task['username'] = user['username']
            result.append(task)
        total[user['id']] = result

    with open('todo_all_employees.json', 'w') as f:
        for el in total:
            json.dump(total, f)

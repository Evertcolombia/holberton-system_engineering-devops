#!/usr/bin/python3
"""
Get the number of suscriptoirs from an
specific subrredit from the reddit api
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ get data form reddit api"""

    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    userA = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0)\
            Gecko/20100101 Firefox/76.0"
    
    headers = {"User-Agent": userA}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response = response.json()
        return response["data"]["subscribers"]
    else:
        return 0

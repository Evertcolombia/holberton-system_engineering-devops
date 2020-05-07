#!/usr/bin/python3


import requests
from sys import argv

def do_request(subreddit, after):

    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'
    userA = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0)\
            Gecko/20100101 Firefox/76.0"

    headers = {"User-Agent": userA}
    response = requests.get(url.format(subreddit, after), headers=headers,
                            allow_redirects=False)

    if response.status_code != 200:
        return None
    res = response.json()
    return res

def recurse(subreddit, hot_list=[], after=''):

    res = do_request(subreddit, after)
    after = res['data']['after']

    if after is not None:
        for post in res['data']['children']:
            hot_list.append(post['data']['title'])
        recurse(subreddit, hot_list, after)
    else: return hot_list


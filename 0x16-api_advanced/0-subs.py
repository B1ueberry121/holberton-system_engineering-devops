#!/usr/bin/python3
''' Queries the Redit API and returns the number of subs '''
import requests


def number_of_subscribers(subreddit):
    ''' Queries the Reddit API and returns the number of subs '''

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
               Safari/537.36"}

    response = requests.get(url, headers=headers).json().get('data')
    if not response:
        return 0

    return response.get('subscribers')

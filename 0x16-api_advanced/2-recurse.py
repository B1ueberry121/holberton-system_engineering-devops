#!/usr/bin/python3
"""
This module defines the following function:
    recurse(subreddit, hot_list=[])
"""
import requests


def recurse(subreddit, hot_list=[], after=1):
    '''
    Returns a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit, return None.
    '''
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    head = {'User-Agent': 'I am a Shield Agent'}
    response = requests.get(url, headers=head, params={'after': after})
    try:
        if response.status_code != 200:
            return None
        if after is None:
            return hot_list
        data_dic = response.json()
        data_list = data_dic['data']['children']
        for value in data_list:
            hot_list.append(value['data']['title'])
        return recurse(subreddit, hot_list, data_dic['data']['after'])
    except:
        pass

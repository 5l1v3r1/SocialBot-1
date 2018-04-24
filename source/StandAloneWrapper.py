#!/usr/bin/python

from api_wrapper.SocialBot import SocialBot
import re

"""
The StandAloneWrapper is a script to implement the behaviour of one bot.
"""

def runBot():
    """
    Create an SocialBot-Object and configure it.
    """
    stb = SocialBot(parseConfig('./config.txt'))
    stb.overwrite_sensitive = False
    algorithm(stb)

def parseConfig(configfile):
    """
    Read the configfile and parse it
    :param configfile:
    """
    cfile = open(configfile, 'r')
    access_info = cfile.read()

    regex = re.compile("(?P<key>[^:\s]+): (?P<arg>[^:\s]+)")

    matches = regex.findall(access_info)
    for match in matches:
        if match[0] == 'consumer_key':
            consumer_key = match[1]
        elif match[0] == 'consumer_secret':
            consumer_secret = match[1]
        elif match[0] == 'access_token':
            access_token = match[1]
        elif match[0] == 'access_token_secret':
            access_token_secret = match[1]

    access_info = {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret,
        'access_token': access_token,
        'access_token_secret': access_token_secret
    }

    return access_info

def algorithm(stb):
    """
    Secifies the behaviour of one or more SocialBot-Objects
    :param stb:
    """
    print(stb.get_tweets("@POTUS"))

runBot()

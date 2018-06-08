from src.twitter import Twitter

# Your access information for the twitter API
access_info = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': ''
}

ptp = Twitter(access_info=access_info)

actions = [
    # Favor a tweet containing 'Ducks are the best!' with the letters in any cases.
    {'exactly': 'Ducks are the best!', 'action': 'favor'},
    # If you want to reply to a tweet which should be case sensitive give it the option case_sensitive.
    # This also works for match and tags.
    {'exactly': 'I WANT A DUCK!', 'options': {'case_sensitive': True}, 'action': 'retweet'},
    # If a tweet matches the match key value by more than 90% answer it.
    {'match': 'Ducks are awesome', 'accuracy': 0.9, 'action': 'reply', 'text': 'You have a typo in there!'},
    # If a tweet contains all of the tags specified favor it.
    {'tags': ['ducks', 'cool'], 'action': 'favor'},
    # You can also use a list to specify your action.
    {'tags': ['ducks', 'the', 'best'], 'action': ['favor', 'follow']}
]

# You can include retweets by with the parameter include_retweets=True
# If you want to limit the actions done simply give it the limit parameter
ptp.react_to_stream(actions, terms=['ducks'], include_retweets=False, limit=1)
ptp.print_thread_info()

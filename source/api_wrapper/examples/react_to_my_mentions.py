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
    # Retweet a mention containing 'hello world!' with the letters in any cases.
    {'exactly': 'Hello world!', 'action': 'retweet'},
    # If you want to reply to a mention which should be case sensitive give it the option case_sensitive.
    # This also works for match and tags.
    {'exactly': 'i WaNt An AnSwER!', 'options': {'case_sensitive': True}, 'action': 'reply', 'text': 'hErE iT iS!'},
    # If a mention matches the match key value by more than 90% answer it.
    {'match': 'Ducks are awesome', 'accuracy': 0.9, 'action': 'reply', 'text': 'You have a typo in there!'},
    # If a mention contains all of the tags specified favor it.
    {'tags': ['politics', 'boring'], 'action': 'favor'},
    # You can also use a list to specify your action.
    {'tags': ['Huskies', 'sweet', 'best'], 'action': ['favor', 'follow']}
]

ptp.react_to_my_mentions(actions)
ptp.print_thread_info()
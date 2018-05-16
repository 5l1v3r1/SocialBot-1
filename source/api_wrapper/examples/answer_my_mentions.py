from src.twitter import Twitter

# Your access information for the twitter API
access_info = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': ''
}

ptp = Twitter(access_info=access_info)

answers = [
    # Answer to a mention containing 'hello world!' with the letters in any cases, with 'The world says hello!'
    {'exactly': 'Hello world!', 'answer': 'The world says hello!'},
    # If you want to answer a mention which should be case sensitive give it the option case_sensitive.
    # This also works for match and tags.
    {'exactly': 'i WaNt An AnSwER!', 'options': {'case_sensitive': True}, 'answer': 'hErE iT iS!'},
    # If a mention matches the match key value by more than 90% answer it.
    {'match': 'Ducks are awesome', 'accuracy': 0.9, 'answer': 'You have a typo in there!'},
    # If a mention contains all of the tags specified answer it with the answer key value.
    {'tags': ['politics', 'boring'], 'answer': 'Yea right! Zzz'}
]

ptp.answer_my_mentions(answers)
ptp.print_thread_info()
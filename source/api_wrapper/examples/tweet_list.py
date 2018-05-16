from src.twitter import Twitter

# Your access information for the twitter API
access_info = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': ''
}

ptp = Twitter(access_info=access_info)

# Tweet 'Hello World!' at the 20th of June 2018 at 19:36:00 (or 7:36:00PM)
list_of_tweets = [
    {'text': 'Hello World!', 'date': '20.06.2018 19:36:00'}
]

# Returns all threads created to tweet your texts at certain dates.
threads = ptp.tweet_list(list_of_tweets)

ptp.print_thread_info()
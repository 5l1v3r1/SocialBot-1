from src.twitter import Twitter

# Your access information for the twitter API
access_info = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': ''
}

ptp = Twitter(access_info=access_info)

# Tweet 'Hello World!'
ptp.tweet(text='Hello World!')

# Search for tweets containing the term 'Hello World!'
status = ptp.search_tweet(term='Hello World!')

# Select the first tweet found and get its id
status_id = status[0].id

# Retweet, favor and reply to that status
ptp.retweet(tweet_id=status_id)
ptp.favor(status_id=status_id)
ptp.reply(status_id=status_id, text='Nice to meet you.')


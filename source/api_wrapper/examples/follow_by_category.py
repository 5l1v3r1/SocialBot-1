from src.twitter import Twitter

# Your access information for the twitter API
access_info = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': ''
}

ptp = Twitter(access_info=access_info)

# Follow all accounts that are listed in the follow suggestion list for politics for the authenticated user.
# The delay argument causes a human-like delay before every follow action. It's a time between 2 and 10 minutes.
# If the delay argument is set to False, all follow actions are executed immediately.
ptp.follow_by_category('Politics', delay=True)

# The standard values for the delay are easily changed like so.
# The values are the time in seconds.
ptp.min_follow_time = 120
ptp.max_follow_time = 600

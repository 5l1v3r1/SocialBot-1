# Python-Twitter-Plus
## Makes building a twitter bot really easy.
This package is build on top of the 'python-twitter' python module.
Look it up [here](https://github.com/bear/python-twitter)!

### Start
At the moment this module is not available on pip. 
If you  want to use it you have to clone the repository and use the following code:

#### If you are on Ubuntu:
```bash
cd /here/should/the/module/be/installed
git clone https://github.com/LukFR/Python-Twitter-Plus.git
sudo pip install -r requirements.txt
```

#### If everything worked you can now import it and start:
Be careful with the import statement if you are not directly working in the project main directory.

```python
from src.twitter import Twitter

# Your access information for the twitter API
access_info = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': ''
}

ptp = Twitter(access_info=access_info)
```

### Activate logging
It's easy to overlook everything your bot is doing. Simply activate logging. For that you need to specify a path where to save the log text file.

```python
# Activate the development mode to see the json responses 
# from twitter in your logs
ptp.development_mode()

# Per default overwrite sensitivity is activated.
# So you can't use the same file twice for logging.
# If you want to change that use:
ptp.overwrite_sensitive = False

# Save the log file in the current directory and call it log
ptp.activate_logging(path='.', name='log')
```

### Tweet, Retweet, Reply and Favor
If you want to tweet, retweet, reply or favor simply call it:
 
 ```python
# Tweet
ptp.tweet(text='Hello World!')

# Now you need a status_id, f.E. from a cute husky video: 992607093160140801

# Retweet
ptp.retweet(status_id=992607093160140801)
# Reply
ptp.reply(status_id=992607093160140801, text='Cute!')
# Favor
ptp.favor(status_id=992607093160140801)
```

### Follow by category
A fast way to follow people recommended for you is to simply use the follow_by_category method.

```python
# The delay argument causes a human-like delay before every follow action. It's a time between 2 and 10 minutes.
# If the delay argument is set to False, all follow actions are executed immediately.
ptp.follow_by_category('Politics', delay=True)
```
### Tweet something at a certain time
With Python-Twitter-Plus this is really easy. Just use the tweet_list function.

```python
# Tweet 'Hello World!' at the 20th of June 2018 at 19:36:00 (or 7:36:00PM)
list_of_tweets = [
    {'text': 'Hello World!', 'date': '20.06.2018 19:36:00'}
]

ptp.tweet_list(list_of_tweets)
```

### Automatically answer your mentions
Here you have 3 options, with which you can specify which mentions you want to answer:
'exactly', 'match' and 'tags'.

```python
answers = [
    # Answer to a mention containing 'hello world!' with the letters in any cases, with 'The world says hello!'
    {'exactly': 'Hello world!', 'answer': 'The world says hello!'},
    # If you want to answer a mention which should be case sensitive give it the option case_sensitive. 
    # This also works for match and tags keys.
    {'exactly': 'i WaNt An AnSwER!', 'options': {'case_sensitive': True}, 'answer': 'hErE iT iS!'},
    # If a mention matches the match key value by more than 90% answer it.
    {'match': 'Ducks are awesome', 'accuracy': 0.9, 'answer': 'You have a typo in there!'},
    # If a mention contains all of the tags specified answer it with the answer key value.
    {'tags': ['politics', 'boring'], 'answer': 'Yea right! Zzz'}
]

ptp.answer_my_mentions(answers)
```

The match option is using the FuzzyWuzzy string matching library.
It's awesome! Look it up [here](https://github.com/seatgeek/fuzzywuzzy)!
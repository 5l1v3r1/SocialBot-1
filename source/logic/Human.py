class Human:
    """

    """
    def __init__(self, twitterobj):
        """
        
        """
        self.twitterobj = twitterobj

    def get_direct_messages(self):
        self.twitterobj.get_my_dms()

    def get_my_timeline(self):
        return self.twitterobj.get_my_timeline()

    def get_timeline_from_user(self, username, user_id=None):
        self.twitterobj.get_tweets(username, user_id)

    def get_my_retweets(self):
        return self.twitterobj.get_my_retweets()

    def get_my_mention(self):
        return self.twitterobj.get_my_mentions()

    def get_followers(self, username=None, user_id=None, page=-1):
        return self.twitterobj.get_followers(username, user_id, page)

    def post_tweet(self, message):
        return self.twitterobj.tweet(text=message)

    def post_Retweet(self, tweet_id):
        return self.twitterobj.retweet(tweet_id)

    def like_tweet(self, status=None, status_id=None):
        return self.twitterobj.favor(status=status, status_id=status_id)

    def follow_User(self, username=None, user_id=None):
        return self.twitterobj.follow(username, user_id)

    def send_direct_message(self, username=None, user_id=None, message=None):
        return self.twitterobj.send_dm(username, user_id, message)

    def search_tweet(self, term):
        return self.twitterobj.search_tweet(term=term)

    def search_user(self, term):
        return self.twitterobj.search_user(term=term)

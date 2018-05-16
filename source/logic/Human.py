class Human:
    """

    """
    def __init__(self, twitterobj):
        """
        
        """
        self.twitterobj = twitterobj

    def get_direct_messages(self):
        self.twitterobj.get_my_dms()

    def get_timeline(self):
        self.twitterobj.get_tweets()

    def get_retweets(self):
        self.twitterobj.get_my_retweets()

    def get_mention(self):
        self.twitterobj.get_my_mentions()

    def get_followers(self, username=None, user_id=None, page=-1):
        self.twitterobj.get_followers(username, user_id, page)

    def create_Account(self):
        # vielleicht nicht möglich
        pass

    def post_tweet(self, message):
        self.twitterobj.tweet(text=message)

    def post_Retweet(self, tweet_id):
        self.twitterobj.retweet(tweet_id)

    def like_tweet(self, status=None, status_id=None):
        self.twitterobj.favor(status=status, status_id=status_id)

    def follow_User(self, username=None, user_id=None):
        self.twitterobj.follow(username, user_id)

    def send_direct_message(self, username=None, user_id=None, message=None):
        self.twitterobj.send_dm(username, user_id, message)

    def search_tweet(self, term):
        return self.twitterobj.search_tweet(term=term)

    def search_user(self, term):
        return self.twitterobj.search_user(term=term)

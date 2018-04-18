import twitter
from source.api_wrapper.Logger import Logger


class SocialBot:
    """
    The SocialBot class is built on top of the twitter module.
    It restricts the functionality of the twitter module and includes logging.
    """

    def __init__(self, access_info):
        """
        Check if access_info contains all necessary information to build an twitter object.
        :param access_info:
        """

        if 'consumer_key' not in access_info:
            raise Exception('Missing consumer_key in access_info')
        elif 'consumer_secret' not in access_info:
            raise Exception('Missing consumer_secret in access_info')
        elif 'access_token' not in access_info:
            raise Exception('Missing access_token in access_info')
        elif 'access_token_secret' not in access_info:
            raise Exception('Missing access_token_secret in access_info')

        self.__api = twitter.Api(
            consumer_key=access_info['consumer_key'],
            consumer_secret=access_info['consumer_secret'],
            access_token_key=access_info['access_token'],
            access_token_secret=access_info['access_token_secret']
        )

        self.overwrite_sensitive = True
        self.__logger = Logger()

    """
    LOG:
    """

    def activate_log(self, path, name):
        """
        Activates the logging via the logger instance.
        :param path:
        :param name:
        :return:
        """

        self.__logger.activate(path, name, self.overwrite_sensitive)

    def __log(self, message):
        """
        Calls the log method of the logger instance.
        :param message:
        :return:
        """

        self.__logger.log(message)

    """
    BASIC ACTIONS:
    """

    def tweet(self, text):
        """
        Tweet a text.
        :param text:
        :return:
        """

        if text == '':
            raise Exception('Missing a tweet text')

        resp = self.__api.PostUpdate(text)
        print(resp)

        self.__log({
            'action': 'Tweeted ' + text,
            'response': str(resp)
        })

    def retweet(self, tweet_id):
        """
        Retweet a tweet with id.
        :param tweet_id:
        :return:
        """

        if (isinstance(tweet_id, str) and tweet_id != '') or (isinstance(tweet_id, int) and tweet_id <= 0):
            raise Exception('Missing tweet_id')

        resp = self.__api.PostRetweet(tweet_id)
        print(resp)

        self.__log({
            'action': 'Retweeted tweet with id "' + tweet_id + '"',
            'response': str(resp)
        })

    def send_dm(self, username='', user_id=None, message=''):
        """
        Send a Direct Message to a user.
        :param username:
        :param user_id:
        :param message:
        :return:
        """

        if username == '' and user_id is None:
            raise Exception('Missing a username or user_id to send a dm')
        elif message == '':
            raise Exception('Missing a message to send a dm')

        if user_id is not None:
            resp = self.__api.PostDirectMessage(message, user_id=user_id, return_json=True)
            log_param = user_id
        else:
            resp = self.__api.PostDirectMessage(message, screen_name=username, return_json=True)
            log_param = user_id

        print(resp)

        self.__log({
            'action': 'Send dm to "' + log_param + '" with text "' + message + '"',
            'response': str(resp)
        })

    """
    SEARCH FUNCTIONS:
    """

    def search_tweet(self, term):
        """
        Search for tweets containing a specified text.
        :param term:
        :return:
        """

        if term == '':
            raise Exception('Missing a search term')

        resp = self.__api.GetSearch(term=term)
        print(resp)

        self.__log({
            'action': 'Searched for tweets containing "' + term + '"',
            'response': str(resp)
        })

    def search_user(self, term):
        """
        Search for a user by username.
        :param term:
        :return:
        """

        if term == '':
            raise Exception('Missing a username to search')

        resp = self.__api.GetUsersSearch(term)
        print(resp)

        self.__log({
            'action': 'Searched for user with term "' + term + '"',
            'response': str(resp)
        })

    """
    GET FUNCTIONS:
    """

    def get_subscriptions(self, username=None, user_id=None):
        """
        Get subscriptions for a user.
        :param user_id:
        :param username:
        :return:
        """

        if username == '' and user_id is None:
            raise Exception('Missing a username or user_id to get subscriptions')

        if username != '' and user_id is not None:
            username = None
            print('Both user_id and username given. Used user_id.')

        resp = self.__api.GetSubscriptions(user_id=user_id, screen_name=username)

        print(resp)

        self.__log({
            'action': 'Got subscriptions for user',
            'user_id': user_id,
            'username': username,
            'response': str(resp)
        })

    def get_tweets(self, username=None, user_id=None):
        """
        Get tweets made by a user.
        :param username:
        :param user_id:
        :return:
        """

        if username == '' and user_id is None:
            raise Exception('Missing a username or user_id to get tweets')

        if username != '' and user_id is not None:
            username = None
            print('Both user_id and username given. Used user_id.')

        resp = self.__api.GetUserTimeline(user_id=user_id, screen_name=username)

        print(resp)

        self.__log({
            'action': 'Got tweets by user',
            'user_id': user_id,
            'username': username,
            'response': str(resp)
        })

    """
    STREAM FUNCTIONS:
    """

    def stream(self, users=None, terms=None):
        """
        Opens a stream to spectate tweets. Can be filtered by users and/or terms.
        Users have to be in the format @[username].
        Both users and terms have to be an array.
        :return:
        """

        self.__log({
            'action': 'Opened Stream',
            'users': str(users),
            'terms': str(terms)
        })

        return self.__api.GetStreamFilter(follow=users, track=terms)

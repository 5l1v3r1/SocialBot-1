import twitter
from source.api_wrapper.Logger import Logger


class SocialBot:

    def __init__(self, access_info):
        """
        :param access_info:

        Check if access_info contains all necessary information to build an twitter object.
        """

        if 'consumer_key' not in access_info:
            raise Exception('Missing consumer_key in access_info')
        elif 'consumer_secret' not in access_info:
            raise Exception('Missing consumer_secret in access_info')
        elif 'access_token' not in access_info:
            raise Exception('Missing access_token in access_info')
        elif 'access_token_secret' not in access_info:
            raise Exception('Missing access_token_secret in access_info')

        self.api = twitter.Api(
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

        resp = self.api.PostUpdate(text)
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

        resp = self.api.PostRetweet(tweet_id)
        print(resp)

        self.__log({
            'action': 'Retweeted tweet with id "' + tweet_id + '"',
            'response': str(resp)
        })

    """
    SEARCH FUNCTIONS:
    """

    def search_tweet(self, text):
        """
        Search for tweets containing a specified text.
        :param text:
        :return:
        """

        if text == '':
            raise Exception('Missing a search term')

        resp = self.api.GetSearch(term=text)
        print(resp)

        self.__log({
            'action': 'Searched for tweets containing "' + text + '"',
            'response': str(resp)
        })

    def search_user(self, username):
        """
        Search for a user by username.
        :param username:
        :return:
        """

        if username == '':
            raise Exception('Missing a username to search')

        resp = self.api.GetUsersSearch(username)
        print(resp)

        self.__log({
            'action': 'Searched for user with name "' + username + '"',
            'response': str(resp)
        })

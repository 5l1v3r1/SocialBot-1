import twitter
import datetime
from pathlib import Path


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

        self.logging = False
        self.logFile = ''
        self.overwrite_sensitive = True

    """
    Activate the action log. Required are a path and a name for the log file.
    It's sensitive for overwritting files and stops if a speficied file already exists.
    """

    def activate_log(self, path, name):
        if path == '':
            raise Exception('Missing path for the logging file')
        elif name == '':
            raise Exception('Missing name for logging file')

        f = Path(path)

        if not f.is_dir():
            raise Exception('The directory "' + path + '" does not exist')

        log_file_path = path + '/' + name + '.txt'
        f = Path(log_file_path)

        if f.exists() and self.overwrite_sensitive:
            raise Exception('The logging file already exists')

        self.logging = True
        self.logFile = path + '/' + name + '.txt'

        file = open(self.logFile, 'a')
        file.write('Log File for SocialBot created on ' + str(datetime.datetime.now()).split('.')[0] + '\n')
        file.write('####' + '\n')
        file.close()

    """
    Logs a message if a log file was specified with activate_log.
    It can handle a simple string or a dict as message object.
    If message is a dict the key and the content are written to the log file.
    Every log to the log file contains a datestamp.
    """

    def log(self, message):
        if self.logging and self.logFile != '':
            if isinstance(message, str):
                f = open(self.logFile, 'a')
                f.write(str(datetime.datetime.now()).split('.')[0] + ' | ' + message + '\n')
                f.write('####' + '\n')
                f.close()

            elif isinstance(message, dict):
                f = open(self.logFile, 'a')
                f.write(str(datetime.datetime.now()).split('.')[0] + ': ' + '\n')
                keys = message.keys()

                for key in keys:
                    f.write(key + ': ' + message[key] + '\n')

                f.write('####' + '\n')
                f.close()

    """
    Tweet a text.
    """

    def tweet(self, text):
        if text == '':
            raise Exception('Missing a tweet text')

        resp = self.api.PostUpdate(text)
        print(resp)

        self.log({
            'action': 'Tweeted ' + text,
            'response': str(resp)
        })

    """
    Search for tweets containing a specified text.
    """

    def search_tweet(self, text):
        if text == '':
            raise Exception('Missing a search term')

        resp = self.api.GetSearch(term=text)
        print(resp)

        self.log({
            'action': 'Searched for tweets containing "' + text + '"',
            'response': str(resp)
        })
import threading
import datetime
from api_wrapper.twitter import Twitter

class Bothandler:
    def __init__(self):
        self.__bot_list = []
    def get_bots(self):
        return self.__bot_list
    def add_bot(self, obj):
        try:
            if type(obj) is Bot:
                self.__bot_list.append(obj)
            else:
                raise TypeError(str(obj) + "This Object isn't from type Bot")
        except TypeError as err:
            raise
    def delete_bot(self, obj):
        try:
            if type(obj) is Bot:
                self.__bot_list.append(obj)
            else:
                raise TypeError(str(obj) + ": " + "This Object isn't from type Bot")
        except TypeError as err:
            raise
    def load_config(self):
        pass

class Human:
    def __init__(self, twitterobj):
        self.twitterobj = twitterobj
    def get_direct_messages(self):
        pass
    def get_timeline(self):
        self.twitterobj.get_tweets()
    def create_Account(self):
        #vielleicht nicht möglich
        pass
    def post_tweet(self, message):
        self.twitterobj.tweet(text=message)
    def post_Retweet(self):
        pass
    def like_tweet(self, status=None, status_id=None):
        self.twitterobj.favor(status=status, status_id=status_id)
    def follow_User(self):
        pass
    def send_direct_message(self):
        pass
    def search_tweet(self, term):
        return self.twitterobj.search_tweet(term=term)
    def search_user(self, term):
        return self.twitterobj.search_user(term=term)

class Bot(Human, threading.Thread):
    def __init__(self, iname, access_info):
        ptp = Twitter(access_info=access_info)
        super().__init__(ptp)
        threading.Thread.__init__(self)
        self.__name = iname
        self.__status = -1
        self.__logbook = Logbook()
        print("Created Bot " + self.name)
    def get_run_status(self):
        return self.__status
    def react_to_direct_message(self):
        print("Message")
    def react_to_tweet(self):
        print("Reacted to Tweet")
    def react_to_retweet(self):
        pass
    def react_to_timeline(self):
        pass
    def run(self):
        print(self.name + " is running...")
        self.__status=0


class Logbook:
    def __init__(self):
        self.__loglist = []
    def add_log(self, obj):
        try:
            if type(obj) is Log:
                    self.__loglist.append(obj)
            else:
                raise TypeError(str(obj) + ": " + "This Object isn't from type Bot")

        except TypeError as err:
            raise
    def get_logs(self):
        return self.__loglist


class Log:
    def __init__(self, message, typ):
        self.__message = message
        self.__typ = typ
        self.__time = datetime.datetime.now()
    def __str__(self):
        return str(self.__time) + " - " + "[" + self.__typ + "] - " + self.__message
    def get_message(self):
        return self.__message


if __name__ == "__main__":
    access_info = {
        'consumer_key': '',
        'consumer_secret': '',
        'access_token': '',
        'access_token_secret': ''
    }

    bothandler = Bothandler()
    bot = Bot("Bot1", access_info)
    bothandler.add_bot(bot)

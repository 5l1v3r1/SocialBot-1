##### FOR TESTING #####
import json
##### FOR TESTING #####
import threading
import datetime
from api_wrapper.src.twitter import Twitter

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
        if type(obj) is Bot:
            self.__bot_list.append(obj)
        else:
            raise TypeError(str(obj) + ": " + "This Object isn't from type Bot")
    def load_config(self):
        pass

class Human(object):
    def __init__(self, twitterobj):
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
        #vielleicht nicht möglich
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

class Bot(Human, threading.Thread):
    def __init__(self, iname, access_info):
        ptp = Twitter(access_info=access_info)
        super().__init__(ptp)
        threading.Thread.__init__(self)
        self.__name = iname
        self.__status = -1
        self.__logbook = Logbook()
        print("Created Bot: " + self.__name)

    def get_run_status(self):
        return self.__status
    def get_name(self):
        return self.__name
    def react_to_direct_message(self):
        print("Message")
    def react_to_tweet(self):
        print("Reacted to Tweet")
    def react_to_retweet(self):
        pass
    def react_to_timeline(self):
        pass
    def run(self):
        print(self.__name + " is running...")
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
    ##### FOR TESTING #####
    config = open("./Config.txt", "r")
    parsed_json = json.loads(config.read())
    config.close()

    access_info = {
        'consumer_key': parsed_json["consumer_key"],
        'consumer_secret': parsed_json["consumer_secret"],
        'access_token': parsed_json["access_token"],
        'access_token_secret': parsed_json["access_token_secret"]
    }

    #parsed_json = json.loads(json_string)

    bothandler = Bothandler()
    bot = Bot("Bot 1", access_info)
    bothandler.add_bot(bot)
    #bothandler.add_bot(bot)
    ##### FOR TESTING #####
import pytest
import threading
import datetime
#package von lukas muss hinzugefügt werden
#from api_wrapper.twitter import Twitter

class Bothandler:
    def __init__(self):
        self.__bot_list = []
    def get_bots(self):
        pass
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
        pass
    def post_Tweet(self, message):
        self.twitterobj.tweet(text=message)
    def post_Retweet(self):
        pass
    def like_Tweet(self, status=None, status_id=None):
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
        self.name = iname
        self.status = -1
        self.logbook = Logbook
        print("Created Bot " + self.name)
    def get_run_status(self):
        return self.status
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
        self.status=0



class Logbook:
    def __init__(self):
        self.loglist = []
    def add_log(self, log):
        if type(log) is Log:
            self.loglist.append(log)
        else:
            print("Logbook: its not a Log Object.")
    def get_logs(self):
        return self.loglist


class Log:
    def __init__(self, message, typ):
        self.__message = message
        self.__typ = typ
        self.__time = datetime.datetime.now()
    def __str__(self):
        return str(self.__time) + " - " + "[" + self.__typ + "] - " + self.__message
    def get_message(self):
        return self.__message

def main():
    access_info = {
        'consumer_key': 'bTlVsty50JzCpJUz71Ntkc7EG',
        'consumer_secret': 'mhM1tAeB352DwmzP2zASRCDmpwMDN0KArFnelnGouoMLgfr4d4',
        'access_token': '986632583999119360-3TYR0QaLuRFUtjgAydQ7Kog8K4Puj1I',
        'access_token_secret': '8ERLDifjUT7a7HA0JOochGu866Tvdx00Cpzb8HjR4TRs3'
    }

    bothandler = Bothandler()
    bot = Bot("Bot1", access_info)
    bothandler.delete_bot(Logbook())


if __name__ == "__main__":
    main()
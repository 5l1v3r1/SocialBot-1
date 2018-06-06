from api_wrapper.src.twitter import Twitter
import threading
from data.Logbook import Logbook
from logic.Human import Human

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

    def react_to_my_mentions(self, input):
        self.twitterobj.react_to_my_mentions(input)

    def react_to_timeline(self):
        self.twitterobj.react_to_my_timeline(input)

    def react_to_stream(self, input, terms, users, limit, include_retweets):
        self.twitterobj.react_to_stream(self, input, terms=terms, users=users, limit=limit, include_retweets=include_retweets)

    def run(self):
        print(self.__name + " is running...")
        self.__status=0
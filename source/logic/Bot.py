import data.Logbook
from api_wrapper.src.twitter import Twitter
import threading
import logic.Human


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

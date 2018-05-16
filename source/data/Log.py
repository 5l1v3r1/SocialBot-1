import datetime


class Log:
    def __init__(self, message, typ):
        self.__message = message
        self.__typ = typ
        self.__time = datetime.datetime.now()

    def __str__(self):
        return str(self.__time) + " - " + "[" + self.__typ + "] - " + self.__message

    def get_message(self):
        return self.__message

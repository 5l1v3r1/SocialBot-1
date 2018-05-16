from logic.Bot import Bot


class Bothandler:
    def __init__(self):
        self.__bot_list = []

    def get_bots(self):
        return self.__bot_listimport

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

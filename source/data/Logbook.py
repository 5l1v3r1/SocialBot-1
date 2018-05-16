import data.Log


class Logbook:
    def __init__(self):
        self.__loglist = []

    def add_log(self, obj):
        try:
            if type(obj) is Log:
                self.__loglist.append(obj)
            else:
                raise TypeError(str(obj) + ': ' + 'This Object isn\'t from type Bot')

        except TypeError as err:
            raise

    def get_logs(self):
        return self.__loglist

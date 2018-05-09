from datetime import datetime
import time


class Helper:
    date_format = '%d.%m.%Y %H:%M:%S'

    @staticmethod
    def get_date_now():
        return datetime.now()

    @staticmethod
    def get_timestamp_now():
        return int(time.time())

    @staticmethod
    def get_date_string_now():
        return datetime.now().strftime(Helper.date_format)

    @staticmethod
    def get_timestamp(date):
        if type(date) == str and date:
            date_obj = datetime.strptime(date, Helper.date_format)
            return int(time.mktime(date_obj.timetuple()))
        elif isinstance(date, datetime):
            return int(time.mktime(date.timetuple()))
        else:
            raise ValueError('Argument date has to be either a string or a datetime obj. Given: ', type(datetime))

    @staticmethod
    def get_date_string_from_timestamp(timestamp):
        return time.strftime(Helper.date_format, time.localtime(timestamp))

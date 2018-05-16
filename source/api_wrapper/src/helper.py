from datetime import datetime
import time
import pytz


class Helper:
    date_format = '%d.%m.%Y %H:%M:%S'
    twitter_date_format = '%a %b %d %H:%M:%S +0000 %Y'

    @staticmethod
    def get_date_now():
        return datetime.now()

    @staticmethod
    def get_timestamp_now():
        return int(time.time())

    @staticmethod
    def get_utc_timestamp_now():
        return int(time.mktime(time.gmtime()))

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

    @staticmethod
    def get_time_stamp_from_twitter_date(date):
        date_obj = datetime.strptime(date, '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)
        return int(time.mktime(date_obj.timetuple()))

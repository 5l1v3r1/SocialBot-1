from threading import Thread, Event
from time import sleep


class StoppableThread(Thread):
    """
    Thread class with a stop() method.
    """

    def __init__(self,  sleep_time=0, target=None, args=(), kwargs=None):
        """
        Call the Thread init method.
        :param sleep_time:
        :param target:
        :param args:
        :param kwargs:
        """
        super().__init__()
        if kwargs is None:
            kwargs = {}

        self.__sleep_time = sleep_time
        self.__sleep_interval = 3
        self.__target = target
        self.__args = args
        self.__kwargs = kwargs
        self.__stop_event = Event()

    def stop(self):
        """
        Method to set the stop flag.
        :return:
        """
        self.__stop_event.set()

    def is_stopped(self):
        """
        Method for a threads to check if a stop flag has been set.
        :return:
        """
        return self.__stop_event.is_set()

    def run(self):
        """
        Override run method from the threading.Thread class.
        Added a regular 'sleep and check if the threads has been stopped' cycle.
        After the elapsed time slept is equal or bigger than the sleep time
        given to the threads as an argument the threads function is started.
        :return:
        """
        __time_slept = 0

        if self.__target:
            while True:
                if __time_slept < self.__sleep_time:
                    if not self.is_stopped():
                        sleep(self.__sleep_interval)
                        __time_slept += self.__sleep_interval
                    else:
                        return
                elif __time_slept >= self.__sleep_time:
                    break

            self.__target(*self.__args, **self.__kwargs)

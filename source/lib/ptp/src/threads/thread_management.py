<<<<<<< HEAD:source/api_wrapper/src/threads/thread_management.py
from src.threads.stoppable_thread import StoppableThread
=======
from lib.ptp.src.threads.stoppable_thread import StoppableThread
>>>>>>> 11e35e95e78125364a542819f0c8a1c8167747b9:source/lib/ptp/src/threads/thread_management.py
from time import sleep


class ThreadManagement:
    """
    The class ThreadManagement is used to keep track of all the threads that a Twitter object currently
    uses.
    """
    def __init__(self):
        """
        __THREAD_POOL:  Every threads created with add_new_thread is collected here.
        __THREAD_INFO:  For every threads created with add_new_thread basic information about the threads is collected
                        here. Basic information are the function name and the arguments for the function.
                        Example element: {'function': 'tweet', 'args': ('Hello World!')}
        """

        self.__THREAD_POOL = []
        self.__THREAD_INFO = []

    def add_new_thread(self, sleep_time=0, f=None, args=None):
        """
        Add a new threads to the threads pool and start it.
        :param sleep_time:
        :param f:
        :param args:
        :return:
        """

        if not f:
            raise ValueError('Missing a function.')
        elif not args:
            raise ValueError('Missing the function arguments.')
        elif f and not callable(f):
            raise ValueError('f has to be a function.')
        elif args and not isinstance(args, tuple):
            raise ValueError('args has to be a tuple.')
        elif sleep_time < 0:
            raise ValueError('sleep_time has to be a positive number.')

        thread = StoppableThread(sleep_time=sleep_time, target=f, args=args)
        self.__THREAD_POOL.append(thread)
        self.__THREAD_INFO.append({'function': f.__name__, 'args': str(args)})
        thread.start()
        return thread

    def get_number_of_threads(self):
        """
        Returns the number of threads in the thread pool.
        :return:
        """

        return len(self.__THREAD_POOL)

    def stop_all_threads(self):
        """
        Stops every threads that's currently in the threads pool.
        :return:
        """

        size = len(self.__THREAD_POOL)

        for i in range(size):
            thread = self.__THREAD_POOL[i]
            thread.stop()
            thread.join()
            print('Thread %s stopped and joined.' % i)

    def clear_thread_pool(self):
        """
        Clears the threads pool from threads elements that are not alive anymore.
        Simultaneously the elements are cleared from threads info.
        :return:
        """

        threads_to_clear = []
        size = len(self.__THREAD_POOL)

        for i in range(size):
            thread = self.__THREAD_POOL[i]
            if not thread.is_alive():
                threads_to_clear.append(i)

        for index in reversed(threads_to_clear):
            del self.__THREAD_POOL[index]
            del self.__THREAD_INFO[index]

    def print_thread_info(self):
        """
        Print every element from threads info.
        :return:
        """
        if len(self.__THREAD_INFO) > 0:
            size = len(self.__THREAD_INFO)

            for i in range(size):
                entry = self.__THREAD_INFO[i]
                print('Thread %s: %s' % (i, entry))
        else:
            print('No threads in thread info.')

    def print_thread_status(self):
        """
        Print the status from every threads in the threads pool.
        :return:
        """

        if len(self.__THREAD_POOL) > 0:
            size = len(self.__THREAD_POOL)
            for i in range(size):
                stopped = 'true' if self.__THREAD_POOL[i].is_stopped() else 'false'
                alive = 'true' if self.__THREAD_POOL[i].is_alive() else 'false'
                daemon = 'true' if self.__THREAD_POOL[i].daemon else 'false'

                print('Thread %s, Stopped: %s, Alive: %s, Daemon: %s' % (i, stopped, alive, daemon))
        else:
            print('No threads in the thread pool.')

    def self_manage_thread(self):
        """
        Managing thread that regularly clears the thread pool.
        :return:
        """

        while True:
            sleep(300)
            self.clear_thread_pool()

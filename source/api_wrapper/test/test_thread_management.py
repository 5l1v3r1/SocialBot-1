import pytest
import threading
from src.threads.thread_management import ThreadManagement


class TestClass(object):
    """
    This TestClass tests both src/threads/stoppable_thread.py and src/threads/thread_management.py
    """
    def test_missing_arguments(self):
        with pytest.raises(ValueError):
            tm = ThreadManagement()
            tm.add_new_thread()

    def test_missing_function(self):
        with pytest.raises(ValueError):
            tm = ThreadManagement()
            tm.add_new_thread(args=('hello',))

    def test_missing_args(self):
        with pytest.raises(ValueError):
            def add(a, b):
                return a + b

            tm = ThreadManagement()
            tm.add_new_thread(f=add)

    def test_negative_sleep_time(self):
        with pytest.raises(ValueError):
            def add(a, b):
                return a + b

            tm = ThreadManagement()
            tm.add_new_thread(sleep_time=-10, f=add, args=(1, 2))

    def test_f_not_callable(self):
        with pytest.raises(ValueError):
            add = 3
            tm = ThreadManagement()
            tm.add_new_thread(sleep_time=10, f=add, args=(1, 2))

    def test_args_no_tuple(self):
        with pytest.raises(ValueError):
            def add(a, b):
                return a + b

            args = [1, 2]
            tm = ThreadManagement()
            tm.add_new_thread(sleep_time=10, f=add, args=args)

    def test_returns_thread(self):
        def add(a, b):
            return a + b

        tm = ThreadManagement()
        assert isinstance(tm.add_new_thread(sleep_time=10, f=add, args=(1, 2)), threading.Thread)

    def test_print_empty_thread_pool(self, capsys):
        tm = ThreadManagement()
        tm.print_thread_info()
        captured = capsys.readouterr()
        assert captured.out == 'No threads in thread info.\n'

        tm.print_thread_status()
        captured = capsys.readouterr()
        assert captured.out == 'No threads in the thread pool.\n'

    def test_print_thread_info(self, capsys):
        tm = ThreadManagement()

        def add(a, b):
            return a + b

        # Test with no thread in the thread pool is in test_print_empty_thread_pools

        tm.add_new_thread(sleep_time=10, f=add, args=(1, 2))
        tm.print_thread_info()
        captured = capsys.readouterr()
        assert captured.out == "Thread 0: {'function': 'add', 'args': '(1, 2)'}\n"

        tm.add_new_thread(sleep_time=10, f=add, args=(2, 3))
        tm.print_thread_info()
        captured = capsys.readouterr()
        assert captured.out == "Thread 0: {'function': 'add', 'args': '(1, 2)'}\nThread 1: "\
                               "{'function': 'add', 'args': '(2, 3)'}\n"

    def test_print_thread_status(self, capsys):
        tm = ThreadManagement()

        def add(a, b):
            return a + b

        # Test with no thread in the thread pool is in test_print_empty_thread_pools

        tm.add_new_thread(sleep_time=10, f=add, args=(1, 2))
        tm.print_thread_status()
        captured = capsys.readouterr()
        assert captured.out == 'Thread 0, Stopped: false, Alive: true, Daemon: false\n'

        tm.add_new_thread(sleep_time=10, f=add, args=(2, 3))
        tm.print_thread_status()
        captured = capsys.readouterr()
        assert captured.out == 'Thread 0, Stopped: false, Alive: true, Daemon: false\nThread 1, Stopped: false, ' \
                               'Alive: true, Daemon: false\n'

    def test_stop_and_clear_threads(self, capsys):
        tm = ThreadManagement()

        def add(a, b):
            return a + b

        tm.add_new_thread(sleep_time=10, f=add, args=(1, 2))
        tm.stop_all_threads()
        captured = capsys.readouterr()
        assert captured.out == 'Thread 0 stopped and joined.\n'

        tm.print_thread_status()
        captured = capsys.readouterr()
        assert captured.out == 'Thread 0, Stopped: true, Alive: false, Daemon: false\n'

        tm.clear_thread_pool()
        tm.print_thread_status()
        captured = capsys.readouterr()
        assert captured.out == 'No threads in the thread pool.\n'

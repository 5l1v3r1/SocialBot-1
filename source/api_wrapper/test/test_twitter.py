import pytest
import os
from pathlib import Path
from src.twitter import Twitter


class TestClass(object):
    # Put in your access information
    access_info = {
        'consumer_key': '',
        'consumer_secret': '',
        'access_token': '',
        'access_token_secret': ''
    }

    def test_access_info(self):
        local_access_info = self.access_info.copy()

        with pytest.raises(ValueError) as ats:
            local_access_info['access_token_secret'] = ''
            Twitter(local_access_info)
        assert 'ValueError: Missing access_token_secret in access_info.' in str(ats)

        with pytest.raises(ValueError) as at:
            local_access_info['access_token'] = ''
            Twitter(local_access_info)
        assert 'ValueError: Missing access_token in access_info.' in str(at)

        with pytest.raises(ValueError) as cs:
            local_access_info['consumer_secret'] = ''
            Twitter(local_access_info)
        assert 'ValueError: Missing consumer_secret in access_info.' in str(cs)

        with pytest.raises(ValueError) as ck:
            local_access_info['consumer_key'] = ''
            Twitter(local_access_info)
        assert 'ValueError: Missing consumer_key in access_info.' in str(ck)

        local_access_info = self.access_info.copy()

        with pytest.raises(ValueError) as need_str:
            local_access_info['consumer_secret'] = 123
            Twitter(local_access_info)
        assert 'ValueError: All values of the access_info dict have to be of type str.' in str(need_str)

    def test_logging(self):
        ptp = Twitter(self.access_info)
        ptp.activate_log('.', 'log')
        log = Path('./log.txt')

        if log.exists():
            log_text = open('./log.txt', 'r').read()
            assert 'Log File for Python-Twitter-Plus. Created on' in log_text
        else:
            assert False

        with pytest.raises(Exception) as existing_log:
            ptp.activate_log('.', 'log')
        assert 'Exception: The logging file already exists.' in str(existing_log)

        os.remove('./log.txt')

    def test_tweet_list(self, capsys):
        ptp = Twitter(self.access_info)
        list_of_tweets = [
            {'text': 'Hello World!', 'date': '20.06.2020 19:36:00'}
        ]
        ptp.tweet_list(list_of_tweets)
        ptp.print_thread_info()
        captured = capsys.readouterr()
        assert ("Thread 0: {'function': '__tweet_at_juncture_thread', 'args': \"('Hello World!'," in captured.out
                and ")\"}\nThread 0, Stopped: false, Alive: true, Daemon: false\n" in captured.out)
        ptp.stop_all_actions()
        ptp.print_thread_info()
        captured = capsys.readouterr()
        assert ('Thread 0 stopped and joined.\nThere are no threads in the thread pool.\n' in captured.out)

    def test_answer_my_mentions(self):
        ptp = Twitter(self.access_info)
        answers = []
        with pytest.raises(ValueError) as no_answers:
            ptp.answer_my_mentions(answers)
        assert 'Missing answers' in str(no_answers)

        with pytest.raises(ValueError) as wrong_answers_type:
            answers = {'content': {}}
            ptp.answer_my_mentions(answers)
        assert 'The argument answers has to be of type list.' in str(wrong_answers_type)

        with pytest.raises(ValueError) as missing_answers_content:
            answers = [{}]
            ptp.answer_my_mentions(answers)
        assert 'The answers dict is missing either the exactly, match or tags key.' in str(missing_answers_content)

        with pytest.raises(ValueError) as empty_exactly:
            answers = [{'exactly': ''}]
            ptp.answer_my_mentions(answers)
        assert 'Found exactly key, but it has no content.' in str(empty_exactly)

        with pytest.raises(ValueError) as empty_match:
            answers = [{'match': ''}]
            ptp.answer_my_mentions(answers)
        assert 'Found match key, but it has no content' in str(empty_match)

        with pytest.raises(ValueError) as empty_tags:
            answers = [{'tags': ''}]
            ptp.answer_my_mentions(answers)
        assert 'Found tags key, but it has no content' in str(empty_tags)

        with pytest.raises(ValueError) as wrong_tags:
            answers = [{'tags': ['hello', '']}]
            ptp.answer_my_mentions(answers)
        assert 'Tags key, has no or wrong content (has to be str).' in str(wrong_tags)

        with pytest.raises(ValueError) as missing_answer:
            answers = [{'exactly': 'hello'}]
            ptp.answer_my_mentions(answers)
        assert 'Missing a answer key' in str(missing_answer)

        with pytest.raises(ValueError) as empty_answer:
            answers = [{'exactly': 'hello', 'answer': ''}]
            ptp.answer_my_mentions(answers)
        assert 'Missing a answer key' in str(empty_answer)

        with pytest.raises(ValueError) as missing_accuracy:
            answers = [{'match': 'hello', 'answer': 'hi!'}]
            ptp.answer_my_mentions(answers)
        assert 'Found match key, missing a accuracy key.' in str(missing_accuracy)

        with pytest.raises(ValueError) as empty_accuracy:
            answers = [{'match': 'hello', 'accuracy': '', 'answer': 'hi!'}]
            ptp.answer_my_mentions(answers)
        assert 'Found accuracy key, but it has no or wrong content (> 1).' in str(empty_accuracy)

        with pytest.raises(ValueError) as wrong_accuracy:
            answers = [{'match': 'hello', 'accuracy': 1.3, 'answer': 'hi!'}]
            ptp.answer_my_mentions(answers)
        assert 'Found accuracy key, but it has no or wrong content (> 1).' in str(wrong_accuracy)

        with pytest.raises(ValueError) as wrong_options:
            answers = [{'exactly': 'hello', 'options': {'wrong_key': True}, 'answer': 'hi there!'}]
            ptp.answer_my_mentions(answers)
        assert 'Unknown key found in options.' in str(wrong_options) and "dict_keys(['wrong_key'])" in str(wrong_options)

        with pytest.raises(ValueError) as case_sensitive:
            answers = [{'exactly': 'hello', 'options': {'case_sensitive': 1}, 'answer': 'hi there!'}]
            ptp.answer_my_mentions(answers)
        assert 'Case_sensitive value has to be of type bool.' in str(case_sensitive)

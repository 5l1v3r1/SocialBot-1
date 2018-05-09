import twitter
import random
import time
from fuzzywuzzy import process
from src.threads.thread_management import ThreadManagement
from src.logger import Logger
from src.helper import Helper


class Twitter:
    """
    The SocialBot class is built on top of the twitter module.
    It restricts the functionality of the twitter module and includes logging.
    The user which is logged in is also called the authenticated user.
    """

    def __init__(self, access_info):
        """
        Check if access_info contains all necessary information to build an twitter object.
        :param access_info:
        """

        if 'consumer_key' not in access_info or not access_info['consumer_key']:
            raise ValueError('Missing consumer_key in access_info.')
        elif 'consumer_secret' not in access_info or not access_info['consumer_secret']:
            raise ValueError('Missing consumer_secret in access_info.')
        elif 'access_token' not in access_info or not access_info['access_token']:
            raise ValueError('Missing access_token in access_info.')
        elif 'access_token_secret' not in access_info or not access_info['access_token_secret']:
            raise ValueError('Missing access_token_secret in access_info.')

        if (type(access_info['consumer_key']) != str or
                type(access_info['consumer_secret']) != str or
                type(access_info['access_token']) != str or
                type(access_info['access_token_secret']) != str):
            raise ValueError('All values of the access_info dict have to be of type str.')

        self.__API = twitter.Api(
            consumer_key=access_info['consumer_key'],
            consumer_secret=access_info['consumer_secret'],
            access_token_key=access_info['access_token'],
            access_token_secret=access_info['access_token_secret']
        )

        self.overwrite_sensitive = True
        self.__development = False
        self.__LOGGER = Logger()
        self.__thread_management = ThreadManagement()

        # min and max response times for tweeting at statuses out of a stream (in secs)
        self.min_response_time = 10
        self.max_response_time = 60

        self.min_follow_time = 120
        self.max_follow_time = 600
        self.__categories = []

    """
    LOG:
    """

    def development_mode(self):
        """
        Activates the development mode.
        If enabled the log of a command contains the responses send by twitter.
        :return:
        """

        if self.__development:
            self.__development = False
            self.__LOGGER.development = False
        else:
            self.__development = True
            self.__LOGGER.development = True

    def activate_log(self, path, name):
        """
        Activates the logging via the logger instance.
        :param path:
        :param name:
        :return:
        """

        self.__LOGGER.activate(path, name, self.overwrite_sensitive)

    def __log(self, message):
        """
        Calls the log method of the logger instance.
        :param message:
        :return:
        """

        self.__LOGGER.log(message)

    """
    GET API OBJECT:
    """

    def get_api_obj(self):
        return self.__API

    """
    BASIC ACTIONS:
    """

    def tweet(self, text):
        """
        Tweet a text.
        :param text:
        :return:
        """

        if not text:
            raise ValueError('Missing a tweet text')
        elif type(text) != str:
            raise ValueError('The tweet text has to be of type str. Given:', type(text))

        resp = self.__API.PostUpdate(text)

        self.__log({
            'action': 'Tweeted a text',
            'text': text,
            'response': str(resp)
        })

        return resp

    def retweet(self, tweet_id):
        """
        Retweet a tweet with id. The id can be either string or int.
        :param tweet_id:
        :return:
        """

        if not tweet_id:
            raise ValueError('Missing tweet_id')
        elif type(tweet_id) != str and type(tweet_id) != int:
            raise ValueError('Tweet_id is neither type str or int. Given: ', type(tweet_id))

        resp = self.__API.PostRetweet(tweet_id)

        self.__log({
            'action': 'Retweeted tweet with id',
            'tweet_id': str(tweet_id),
            'response': str(resp)
        })

        return resp

    def reply(self, status_id, message):
        """
        Reply to a status with a message.
        :param status_id:
        :param message:
        :return:
        """

        if not status_id:
            raise ValueError('Missing a status_id')
        elif type(status_id) != str and type(status_id) != int:
            raise ValueError('Status_id is neither type str or int. Given: ', type(status_id))
        elif not message:
            raise ValueError('Missing a tweet text')
        elif type(message) != str:
            raise ValueError('The tweet text has to be of type str. Given:', type(message))

        resp = self.__API.PostUpdate(message, in_reply_to_status_id=status_id)

        self.__log({
            'action': 'Replied to a status.',
            'message': message,
            'status_id': str(status_id),
            'response': str(resp)
        })

        return resp

    def favor(self, status=None, status_id=None):
        """
        Favor a status as authenticated user.
        :return:
        """

        if not status and not status_id:
            raise ValueError('Missing a status or status_id to favor.')

        resp = self.__API.CreateFavorite(status=status, status_id=status_id)

        self.__log({
            'action': 'Favored a tweet',
            'status': str(status),
            'status_id': str(status_id),
            'response': str(resp)
        })

        return resp

    def send_dm(self, username=None, user_id=None, message=None):
        """
        Send a Direct Message to a user. If both username and user_id are not None the twitter module
        only uses the user_id.
        :param username:
        :param user_id:
        :param message:
        :return:
        """

        if not username and not user_id:
            raise ValueError('Missing a username or user_id to send a dm')
        elif (username and type(username) != str) or (user_id and (type(user_id) != str and type(user_id) != int)):
            raise ValueError('Username has to be str. User_id can be str or int. Given:', type(user_id), type(username))
        elif not message:
            raise ValueError('Missing a message to send a dm')
        elif type(message) != str:
            raise ValueError('The message has to be of type str. Given:', type(message))

        resp = self.__API.PostDirectMessage(text=message, user_id=user_id, screen_name=username, return_json=True)

        self.__log({
            'action': 'Send dm to user',
            'message': message,
            'user_id': str(user_id),
            'username': str(username),
            'response': str(resp)
        })

        return resp

    def follow(self, username=None, user_id=None):
        """
        Follow a user specified by username or user_id.
        :param username:
        :param user_id:
        :return:
        """

        if not username and not user_id:
            raise ValueError('Missing a username or a user_id to follow.')
        elif (username and type(username) != str) or (user_id and (type(user_id) != str and type(user_id) != int)):
            raise ValueError('Username has to be str. User_id can be str or int. Given:', type(user_id), type(username))

        resp = self.__API.CreateFriendship(user_id=user_id, screen_name=username)

        self.__log({
            'action': 'Followed a user.',
            'username': str(username),
            'user_id': str(user_id),
            'response': str(resp)
        })

    """
    SEARCH FUNCTIONS:
    """

    def search_tweet(self, term):
        """
        Search for tweets containing a specified text.
        :param term:
        :return:
        """

        if not term:
            raise ValueError('Missing a search term')
        elif type(term) != str:
            raise ValueError('Search Term has to be of type str. Given: ', type(term))

        resp = self.__API.GetSearch(term=term)

        self.__log({
            'action': 'Searched for tweets containing "' + term + '"',
            'response': str(resp)
        })

        return resp

    def search_user(self, term):
        """
        Search for a user by username.
        :param term:
        :return:
        """

        if not term:
            raise ValueError('Missing a username to search')
        elif type(term) != str:
            raise ValueError('Search Term has to be of type str. Given: ', type(term))

        resp = self.__API.GetUsersSearch(term)

        self.__log({
            'action': 'Searched for user with term "' + term + '"',
            'response': str(resp)
        })

        return resp

    """
    GET FUNCTIONS:
    """

    def get_subscriptions(self, username=None, user_id=None, count=20, page=-1):
        """
        Get subscriptions for a user. If both username and user_id are not None the twitter module
        only uses the user_id.
        :param count:
        :param page:
        :param user_id:
        :param username:
        :return:
        """

        if not username and not user_id:
            raise ValueError('Missing a username or user_id to get subscriptions')
        elif (username and type(username) != str) or (user_id and (type(user_id) != str and type(user_id) != int)):
            raise ValueError('Username has to be str. User_id can be str or int. Given:', type(user_id), type(username))

        resp = self.__API.GetSubscriptions(user_id=user_id, screen_name=username, count=count, cursor=page)

        self.__log({
            'action': 'Got subscriptions for user',
            'user_id': str(user_id),
            'username': str(username),
            'response': str(resp)
        })

        return resp

    def get_tweets(self, username=None, user_id=None):
        """
        Get tweets made by a user. If both username and user_id are not None the twitter module
        only uses the user_id.
        :param username:
        :param user_id:
        :return:
        """

        if not username and not user_id:
            raise ValueError('Missing a username or user_id to get tweets')
        elif (username and type(username) != str) or (user_id and (type(user_id) != str and type(user_id) != int)):
            raise ValueError('Username has to be str. User_id can be str or int. Given:', type(user_id), type(username))

        resp = self.__API.GetUserTimeline(user_id=user_id, screen_name=username)

        self.__log({
            'action': 'Got tweets by user',
            'user_id': str(user_id),
            'username': str(username),
            'response': str(resp)
        })

        return resp

    def get_followers(self, username=None, user_id=None, page=-1):
        """
        Get max. 200 followers for a certain user on one page.
        If both username and user_id are not None the twitter module
        only uses the user_id.
        :param page:
        :param username:
        :param user_id:
        :return:
        """

        if not username and not user_id:
            raise ValueError('Missing a username or user_id to get followers')
        elif (username and type(username) != str) or (user_id and (type(user_id) != str) and type(user_id) != int):
            raise ValueError('Username has to be str. User_id can be str or int. Given:', type(user_id), type(username))

        resp = self.__API.GetFollowersPaged(user_id=user_id, screen_name=username, cursor=page)

        self.__log({
            'action': 'Got followers for user',
            'username': str(username),
            'user_id': str(user_id),
            'page': str(page),
            'response': str(resp)
        })

        return resp

    """
    GET FUNCTIONS (FOR AUTHENTICATED USER):
    """

    def get_my_replies(self):
        """
        Gets the most recent replies for the authenticated user.
        :return:
        """

        resp = self.__API.GetReplies()

        self.__log({
            'action': 'Got replies of authenticated user',
            'response': str(resp)
        })

        return resp

    def get_my_retweets(self):
        """
        Gets the most recent retweets of tweets made by the authenticated user.
        :return:
        """

        resp = self.__API.GetRetweetsOfMe()

        self.__log({
            'action': 'Got retweets of tweets made by the authenticated user',
            'response': str(resp)
        })

        return resp

    def get_my_mentions(self):
        """
        Gets the most recent mentions of the authenticated user.
        :return:
        """

        resp = self.__API.GetMentions()

        self.__log({
            'action': 'Got mentions of the authenticated user.',
            'response': str(resp)
        })

        return resp

    """
    STREAM FUNCTIONS:
    """

    def stream(self, users=None, terms=None):
        """
        Opens a stream to spectate tweets. Has to be filtered by users and/or terms.
        Users should be as user_id.
        Both users and terms have to be an array.
        :param users:
        :param terms:
        :return:
        """

        if not users and not terms:
            raise ValueError('Missing users or terms.')
        elif (users and type(users) != list) or (terms and type(terms) != list):
            raise ValueError('Both users and terms have to be of type list/array. Given:', type(users), type(terms))

        self.__log({
            'action': 'Opened Stream',
            'users': str(users),
            'terms': str(terms)
        })

        return self.__API.GetStreamFilter(follow=users, track=terms)

    def limit_stream(self, users=None, terms=None, limit=None):
        """
        Opens a stream to spectate tweets. Has to be filtered by users and/or terms.
        Users should be as user_id.
        Both users and terms have to be an array.
        :param users:
        :param terms:
        :param limit:
        :return:
        """

        if not users and not terms:
            raise ValueError('Missing users or terms.')
        elif (users and type(users) != list) or (terms and type(terms) != list):
            raise ValueError('Both users and terms have to be of type list/array. Given:', type(users), type(terms))
        elif not limit:
            raise ValueError('Missing a limit.')
        elif limit and type(limit) != int:
            raise ValueError('Limit has to be of type int.')

        stream = self.__API.GetStreamFilter(follow=users, track=terms)
        result = []

        for item in stream:
            if len(result) < limit:
                result.append(item)
            else:
                break

        return result

    def tweet_at_stream(self, message, nth_tweet=None, users=None, terms=None, limit=None):
        """
        Opens a limit_stream and tweets a message at a specified tweet. Every tweet has a response time that is between
        min_response_time and max_response_time. The response time is a waiting time before a text is tweeted.
        :param message:
        :param nth_tweet:
        :param users:
        :param terms:
        :param limit:
        :return:
        """

        if not message:
            raise ValueError('Missing a message.')
        elif message and type(message) != str:
            raise ValueError('Message has to be of type str. Given: ', type(message))
        elif not nth_tweet and nth_tweet != 0:
            raise ValueError('Missing a tweet pointer on the stream.')
        elif nth_tweet and type(nth_tweet) != int:
            raise ValueError('Nth_tweet has to be of type int. Given: ', type(nth_tweet))
        elif not users and not terms:
            raise ValueError('Missing users or terms.')
        elif (users and type(users) != list) or (terms and type(terms) != list):
            raise ValueError('Both users and terms have to be of type list/array. Given:', type(users), type(terms))
        elif not limit:
            raise ValueError('Missing a limit.')
        elif limit and type(limit) != int:
            raise ValueError('Limit has to be of type int.')
        elif limit <= nth_tweet:
            raise ValueError('nth_tweet has to be smaller than the limit.')

        thread = self.__thread_management.add_new_thread(target=self.__tweet_at_stream_thread,
                                                         args=(message, nth_tweet, users, terms, limit))

        return thread

    """
    EXTENDING FUNCTIONS:
    """

    def tweet_list(self, list_of_tweets):
        """
        Tweets a list of tweets. Every item in the list_of_tweets has to have a date. For every item in the list of
        tweets a threads is started. The tweet has no response time and is tweeted exactly at the date specified.
        Every threads gets a sleep_duration time in seconds and sleeps for the duration.
        :param list_of_tweets:
        :return:
        """

        thread_args = []
        result = []

        if not list_of_tweets:
            raise ValueError('list_of_tweets is missing.')
        elif list_of_tweets and type(list_of_tweets) != list:
            raise ValueError('list_of_tweets has to be a list.')

        for item in list_of_tweets:
            if not item['text']:
                raise ValueError('Missing a text to tweet in the list_of_tweets')
            elif not item['date']:
                raise ValueError('Missing a date to tweet in the list_of_tweets')
            elif item['text'] and item['date']:
                # Returns Unix timestamp
                timestamp = Helper.get_timestamp(item['date'])
                now = Helper.get_timestamp_now()

                if timestamp > now:
                    sleep_dur = timestamp - now
                else:
                    raise ValueError('Can\'t tweet in the past. Date has to be in the future. At item:', item['text'],
                                     item['date'])

                thread_args.append({'sleep_duration': sleep_dur, 'text': item['text']})

        for item in thread_args:
            thread = self.__thread_management.add_new_thread(sleep_time=item['sleep_duration'],
                                                             f=self.__tweet_at_juncture_thread,
                                                             args=(item['text'], item['sleep_duration']))
            result.append(thread)

        self.__log({
            'action': 'Tweeted a list. Started threads.',
            'list_of_tweets': str(list_of_tweets),
            'number_of_threads': len(result),
            'result': str(result)
        })

        return result

    def follow_by_category(self, category, delay=True):
        """
        Follow users that are in a specified category.
        Between every follow action there is a delay between the min_follow_time
        and the max_follow_time (standard: 2 - 10 minutes).
        If the delay argument is set to False, the follow actions are executed immediately.
        :param category:
        :param delay:
        :return:
        """

        if not category:
            raise ValueError('Missing a category.')
        elif category and type(category) != str:
            raise ValueError('Category has to be of type str. Given: ', type(category))

        self.__categories = self.__API.GetUserSuggestionCategories()

        self.__thread_management.add_new_thread(f=self.__manage_follow_category,
                                                       args=(category, delay))

    """
    TWEET THREAD FUNCTIONS:
    """

    def __tweet_at_juncture_thread(self, text=None, sleep_duration=None):
        """
        This threads function tweets a text at a certain moment specified by the sleep_duration.
        The sleep_duration argument in this function is just for log purposes. The waiting/sleeping
        is done with the ThreadManagement.add_new_thread sleep_time argument.
        :param text:
        :return:
        """

        resp = self.tweet(text)

        self.__log({
            'action': 'Tweeted at juncture',
            'text': text,
            'sleep_duration': sleep_duration,
            'response': str(resp)
        })

        return resp

    """
    STREAM THREAD FUNCTIONS:
    """

    def __tweet_at_stream_thread(self, message, nth_tweet=None, users=None, terms=None, limit=None):
        """
        This threads function tweets at a certain tweet of a stream.
        :param message:
        :param nth_tweet:
        :param users:
        :param terms:
        :param limit:
        :return:
        """

        stream = self.stream(users=users, terms=terms)

        stream_results = []
        reply_results = []

        for item in stream:
            if len(stream_results) < limit:
                print(item)
                stream_results.append(item)
            else:
                break

        if nth_tweet == -1:
            for status in stream_results:
                time.sleep(random.uniform(self.min_response_time, self.max_response_time))
                reply_results.append(self.reply(status['id'], message))
        elif nth_tweet != -1:
            status = stream_results[nth_tweet]
            time.sleep(random.uniform(self.min_response_time, self.max_response_time))
            reply_results.append(self.reply(status['id'], message))

        self.__log({
            'action': 'Tweeted at stream',
            'message': message,
            'nth_tweet': str(nth_tweet),
            'users': str(users),
            'terms': str(terms),
            'limit': str(limit),
            'response': str(reply_results)
        })

        return reply_results

    """
    FOLLOW THREAD FUNCTIONS:
    """

    def __manage_follow_category(self, category, delay=True):
        """
        Manages the follow queue. Creates a thread for every person to follow.
        :param category:
        :param delay:
        :return:
        """

        category_names = []
        category_obj = twitter.Category()
        follow_queue = []

        for item in self.__categories:
            category_names.append(item.name)

        best = process.extractOne(category, category_names)

        # If a subject is already in the category_names list change the slug.

        if best[1] > 90:
            print('Found a very similar named category. Changed the category to: %s' % best[0])
            i = category_names.index(best[0])
            category_obj.slug = self.__categories[i].slug
        else:
            category_obj.slug = category

        try:
            people_to_follow = self.__API.GetUserSuggestion(category=category_obj)
            time_sum = 0

            for account in people_to_follow:
                if delay:
                    time_sum += int(random.uniform(self.min_follow_time, self.max_follow_time))

                follow_queue.append({
                    "info": account,
                    "date": Helper.get_date_string_from_timestamp(Helper.get_timestamp_now() + time_sum)
                })

                self.__thread_management.add_new_thread(sleep_time=time_sum,
                                                        f=self.follow,
                                                        args=(None, account.id))
            print(follow_queue)

        except twitter.TwitterError as err:
            if 'Sorry, that page does not exist.' in err:
                print('Could not find anything for the category %s' % category_obj.slug)
                return False

    """
    THREAD HANDLING FUNCTIONS:
    """

    def stop_all_actions(self):
        """
        Stop all threads that are sleeping. F.E. a tweet_list thread.
        :return:
        """

        self.__thread_management.stop_all_threads()
        self.__thread_management.clear_thread_pool()

    def print_thread_info(self):
        """
        Prints every information about the threads currently in the thread pool.
        :return:
        """

        if self.__thread_management.get_number_of_threads() > 0:
            self.__thread_management.print_thread_info()
            self.__thread_management.print_thread_status()
        else:
            print('There are no threads in the thread pool.')

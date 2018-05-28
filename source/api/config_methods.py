from api.api_error import APIError
from api.api_message import APIMessage
from api.json_connector import JSONConnector
from api.api_config import APIConfig
from api.api_oauth import OAuthProcess
import json
import asyncio


class ConfigMethods:

    @staticmethod
    def add_app(req):
        keys = req.keys()

        if 'app_name' not in keys:
            return APIError.create(message='Missing a name in the request body.', code=400)
        elif 'consumer_key' not in keys:
            return APIError.create(message='Missing a consumer key in the request body.', code=400)
        elif 'consumer_secret' not in keys:
            return APIError.create(message='Missing a consumer secret in the request body.', code=400)
        else:
            apps = JSONConnector.get_json_file_content(
                directory=APIConfig.json_save_path,
                name=APIConfig.json_apps_file_name
            )

            app = {
                'app_name': req['app_name'],
                'consumer_key': req['consumer_key'],
                'consumer_secret': req['consumer_secret']
            }

            if apps:
                for u in apps['apps']:
                    if u['app_name'] == app['app_name']:
                        return APIError.create(message='User with that app name already exists.', code=400)
                    elif u['consumer_key'] == app['consumer_key']:
                        return APIError.create(message='User with that consumer key already exists.', code=400)
                    elif u['consumer_secret'] == app['consumer_secret']:
                        return APIError.create(message='User with that consumer secret already exists.', code=400)

                apps['apps'].append(app)
            else:
                apps = {'apps': [app]}

            JSONConnector.set_json_file_content(
                directory=APIConfig.json_save_path,
                name=APIConfig.json_apps_file_name,
                data=apps
            )

            return APIMessage.create(message='Successfully added app.', code=200)

    @staticmethod
    def add_bot(req):
        keys = req.keys()

        if 'app_name' not in keys:
            return APIError.create(message='Missing a app name in the request body.', code=400)

        apps = JSONConnector.get_json_file_content(
            directory=APIConfig.json_save_path,
            name=APIConfig.json_apps_file_name
        )

        consumer_key = ''
        consumer_secret = ''

        for item in apps['apps']:
            if item['app_name'] == req['app_name']:
                consumer_key = item['consumer_key']
                consumer_secret = item['consumer_secret']

        if consumer_key and consumer_secret:
            oauth_data = OAuthProcess.start_oauth(consumer_key, consumer_secret)
            oauth_data['app_name'] = req['app_name']
            return APIMessage.create(message='Started OAuth process.', code=200, dump=oauth_data)
        else:
            return APIError.create(message='Something went wrong.', code=400)

    @staticmethod
    def add_bot_pin(req):
        keys = req.keys()

        if 'consumer_key' not in keys:
            return APIError.create(message='Missing a consumer key in the request body.', code=400)
        elif 'consumer_secret' not in keys:
            return APIError.create(message='Missing a consumer secret in the request body.', code=400)
        elif 'oauth_token' not in keys:
            return APIError.create(message='Missing a oauth token in the request body.', code=400)
        elif 'oauth_token_secret' not in keys:
            return APIError.create(message='Missing a oauth token secret in the request body.', code=400)
        elif 'pin_code' not in keys:
            return APIError.create(message='Missing a pin code in the request body.', code=400)
        elif 'bot_name' not in keys:
            return APIError.create(message='Missing a bot name in the request body.', code=400)
        elif 'app_name' not in keys:
            return APIError.create(message='Missing a app name in the request body.', code=400)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(OAuthProcess.confirm_with_pin(
            req['consumer_key'],
            req['consumer_secret'],
            req['oauth_token'],
            req['oauth_token_secret'],
            req['pin_code']
        ))
        loop.close()

        if result:
            if 'access_token' in result and 'access_token_secret' in result:
                bots = JSONConnector.get_json_file_content(
                    directory=APIConfig.json_save_path,
                    name=APIConfig.json_bots_file_name
                )

                bot = {
                    'bot_name': req['bot_name'],
                    'access_token': result['access_token'],
                    'access_token_secret': result['access_token_secret'],
                    'app_name': req['app_name'],
                    'consumer_key': req['consumer_key'],
                    'consumer_secret': req['consumer_secret']
                }

                if bots:
                    for u in bots['users']:
                        if u['bot_name'] == bot['bot_name']:
                            return APIError.create(message='Bot with that botname already exists.', code=400)
                        elif u['access_token'] == bot['access_token']:
                            return APIError.create(message='Bot with that access token already exists.', code=400)
                        elif u['access_token_secret'] == bot['access_token_secret']:
                            return APIError.create(message='Bot with that access token secret already exists.',
                                                   code=400)

                    bots['bots'].append(bot)
                else:
                    bots = {'bots': [bot]}

                JSONConnector.set_json_file_content(
                    directory=APIConfig.json_save_path,
                    name=APIConfig.json_bots_file_name,
                    data=bots
                )

                return APIMessage.create(message='Successfully added bot.', code=200)
            else:
                return APIError.create(message='Something went wrong.', code=400)
        else:
            return APIError.create(message='Something went wrong.', code=400)


    @staticmethod
    def get_users():
        users = JSONConnector.get_json_file_content(
            directory=APIConfig.json_save_path,
            name=APIConfig.json_users_file_name
        )

        if users:
            return json.dumps(users)
        else:
            return APIError.create(message='No users configured.', code=400)

    @staticmethod
    def get_bots():
        bots = JSONConnector.get_json_file_content(
            directory=APIConfig.json_save_path,
            name=APIConfig.json_bots_file_name
        )

        if bots:
            return json.dumps(bots)
        else:
            return APIError.create(message='No bots configured.', code=400)

    @staticmethod
    def get_apps():
        apps = JSONConnector.get_json_file_content(
            directory=APIConfig.json_save_path,
            name=APIConfig.json_apps_file_name
        )

        if apps:
            return json.dumps(apps)
        else:
            return APIError.create(message='No apps configured.', code=400)


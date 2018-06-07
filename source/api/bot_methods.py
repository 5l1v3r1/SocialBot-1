from api.api_error import APIError
from api.api_message import APIMessage
from api.json_connector import JSONConnector
from api.api_config import APIConfig
from api.ptp_connector import PTPConnector


class BotMethods:

    @staticmethod
    def start_bot(req):
        """
        Starts a PTP Bot object.
        :param req:
        :return:
        """
        keys = req.keys()

        if 'bot_name' not in keys or not req['bot_name']:
            return APIError.create(message='No bot name in the request body.', code=400)
        elif 'action_name' not in keys or not req['action_name']:
            return APIError.create(message='No action name in the request body.', code=400)

        bots = JSONConnector.get_json_file_content(
            directory=APIConfig.json_save_path,
            name=APIConfig.json_bots_file_name
        )

        bot_actions = JSONConnector.get_json_file_content(
            directory=APIConfig.json_save_path,
            name=APIConfig.json_bot_actions_file_name
        )

        found_action = {}
        found_bot = {}

        for item in bot_actions['bot_actions']:
            print(req, item)
            if req['bot_name'] == item['bot_name'] and req['action_name'] == item['action_name']:
                found_action = item

        for item in bots['bots']:
            if req['bot_name'] == item['bot_name']:
                found_bot = item

        if found_action and found_bot:
            access_info = {
                'access_token': found_bot['access_token'],
                'access_token_secret': found_bot['access_token_secret'],
                'consumer_key': found_bot['consumer_key'],
                'consumer_secret': found_bot['consumer_secret']
            }

            PTPConnector.start_bot(access_info, found_action['method'], {'actions': found_action['actions']})

            return APIMessage.create(message='Bot successfully started.', code=200)

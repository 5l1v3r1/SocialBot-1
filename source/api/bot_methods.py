from api.api_error import APIError
from api.api_message import APIMessage
from api.json_connector import JSONConnector
from api.api_config import APIConfig
from api.api_oauth import OAuthProcess
import json

class BotMethods:

    @staticmethod
    def start_bot(req):
        keys = req.keys()

        if 'bot_name' not in keys or not req['bot_name']:
            return APIError.create(message='No bot name in the request body.', code=400)
        elif 'action_name' not in keys or not req['action_name']:
            return APIError.create(message='No action name in the request body.', code=400)

        bot_actions = JSONConnector.get_json_file_content(
            directory=APIConfig.json_save_path,
            name=APIConfig.json_bots_actions_file_name
        )

        for item in bot_actions:
            if req['bot_name'] == item['bot_name'] and req['action_name'] == item['action_name']:
                

from api.config_methods import ConfigMethods
from api.api_error import APIError
from api.bot_methods import BotMethods


class API:
    @staticmethod
    def test(request):
        """
        Basic API test method.
        :param request:
        :return:
        """
        if request:
            print(request)
            print(request.get_json())
        return 'Everything is working'

    @staticmethod
    def test_request_return_req(request):
        """
        Tests if a request is valid.
        :param request:
        :return:
        """

        if not request:
            return APIError.create(message='Missing a request body.', code=400)
        print(request)
        req = request.get_json()
        keys = req.keys()

        if 'action' not in keys:
            return APIError.create(message='Missing a action in the request body.', code=400)

        return {
            'req': req,
            'keys': keys
        }

    @staticmethod
    def bot(request):
        """
        Methods used by the bot endpoint of the API.
        :param request:
        :return:
        """

        res = API.test_request_return_req(request)

        if type(res) != dict:
            return res

        req = res['req']
        act = req['action']

        if act == 'start_bot':
            return BotMethods.start_bot(req)
        elif act == 'stop_bot':
            return 
        else:
            return APIError.create(message='Action given in request body is unknown.', code=400)

    @staticmethod
    def config(request):
        """
        Methods used by the config endpoint of the API.
        :param request:
        :return:
        """

        res = API.test_request_return_req(request)

        if type(res) != dict:
            return res

        req = res['req']
        act = req['action']

        if act == 'add_app':
            return ConfigMethods.add_app(req)
        elif act == 'add_bot':
            return ConfigMethods.add_bot(req)
        elif act == 'add_bot_pin':
            return ConfigMethods.add_bot_pin(req)
        elif act == 'get_bots':
            return ConfigMethods.get_bots()
        elif act == 'get_apps':
            return ConfigMethods.get_apps()
        elif act == 'get_bot_actions':
            return ConfigMethods.get_bot_actions()
        elif act == 'configure_bot':
            return ConfigMethods.configure_bot(req)
        else:
            return APIError.create(message='Action given in request body is unknown.', code=400)

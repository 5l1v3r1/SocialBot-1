from datetime import datetime
from api.api_config import APIConfig
from lib.ptp.src.twitter import Twitter


class PTPConnector:
    @staticmethod
    def start_bot(access_info, method, args):
        """
        Creates an PTP object and starts it.
        :param access_info:
        :param method:
        :param args:
        :return:
        """

        ptp = Twitter(access_info)
        ptp.development_mode()
        ptp.overwrite_sensitive = False
        ptp.activate_log(path=APIConfig.log_save_path, name='log-' + datetime.now().strftime('%d/%m/%Y_%H-%M-%S'))

        if method == 'react_to_my_timeline':
            actions = args['actions']
            ptp.react_to_my_timeline(actions)
        elif method == 'react_to_my_mentions':
            actions = args['actions']
            ptp.react_to_my_mentions(actions)

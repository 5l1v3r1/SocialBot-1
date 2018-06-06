from source.gui.ptp.src import twitter
from api.api_config import APIConfig


class PTPConnector:
    @staticmethod
    def create_bot(bot_name=None):
        return
    def start_bot(access_info, method, args):
        ptp = Twitter(access_info)
        ptp.development_mode()
        ptp.overwrite_sensitive = False
        ptp.activate_logging(path=APIConfig.log_save_path, name='log')

        if method == 'react_to_my_timeline':
            actions = args['actions']
            ptp.react_to_my_timeline(actions)
        elif method == 'react_to_my_mentions':
            actions = args['actions']
            ptp.react_to_my_mentions(actions)

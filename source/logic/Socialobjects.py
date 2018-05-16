##### FOR TESTING #####
import json
##### FOR TESTING #####
from logic.Bot import Bot
from logic.Bothandler import Bothandler

if __name__ == "__main__":
    ##### FOR TESTING #####
    config = open("./logic/Config.txt", "r")
    parsed_json = json.loads(config.read())
    config.close()

    access_info = {
        'consumer_key': parsed_json["consumer_key"],
        'consumer_secret': parsed_json["consumer_secret"],
        'access_token': parsed_json["access_token"],
        'access_token_secret': parsed_json["access_token_secret"]
    }

    #parsed_json = json.loads(json_string)

    bothandler = Bothandler()
    bot = Bot("Bot 1", access_info)
    bothandler.add_bot(bot)
    #bothandler.add_bot(bot)
    ##### FOR TESTING #####

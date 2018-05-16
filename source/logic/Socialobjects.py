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
    #test = bot.post_tweet("sdf Again")
    #print(test)
    print(bot.get_timeline())
    #test2 = bot.like_tweet("996761793681854465")
    #print(test2)
    #print(type(test2))
    #bothandler.add_bot(bot)
    ##### FOR TESTING #####

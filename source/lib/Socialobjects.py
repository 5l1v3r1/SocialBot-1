import threading
import datetime

class Bothandler:
    def __init__(self):
        self.botList = []
    def getBots(self):
        pass
    def addBot(self):
        pass
    def deleteBot(self):
        pass
    def loadConfig(self):
        pass

class Human:
    def __init__(self):
        pass
    def getFirstname(self):
        pass
    def getLastname(self):
        pass
    def getEmail(self):
        pass
    def getDirectMessages(self):
        pass
    def getTimeline(self):
        pass
    def createAccount(self):
        pass
    def postTweet(self):
        pass
    def postRetweet(self):
        pass
    def likeTweet(self):
        pass
    def followUser(self):
        pass
    def sendDirectMessage(self):
        pass
    def searchTweet(self):
        pass

class Bot(Human, threading.Thread):
    def __init__(self, iname):
        super().__init__()
        threading.Thread.__init__(self)
        self.name = iname
        self.status = -1
        self.logbook = Logbook
        print("Created Bot" + self.name)
        
    def getStatus(self):
        return self.status

    def reactToDirectMessage(self):
        print("Message")

    def reactToTweet(self):
        print("Reacted to Tweet")

    def reactToRetweet(self):
        pass

    def reactToTimeline(self):
        pass

    def run(self):
        print(self.name + " is running...")
        self.status=0

class Logbook:
    def __init__(self):
        self.loglist = []
    def addLog(self, log):
        if type(log) is Log:
            self.loglist.append(log)
        else:
            print("Logbook: its not a Log Object.")
    def getLogs(self):
        return self.loglist


class Log:
    def __init__(self, message, typ):
        self.__message = message
        self.__typ = typ
        self.__time = datetime.datetime.now()
    def __str__(self):
        return str(self.__time) + " - " + "[" + self.__typ + "] - " + self.__message
    def getMessage(self):
        return self.__message

def main():
    logbook = Logbook()
    log = Log("Meine Nachricht", "TEST")
    logbook.addLog(log)
    del log

    print(logbook.getLogs())


if __name__ == "__main__":
    main()
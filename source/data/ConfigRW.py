import xml.etree.ElementTree
import pickle


class configRW:
    """Class for Read / Write operations with config-files."""

    def __init__(self, file):
        """
        Read the confg from a given xml-files.

        :param file:
        """
        self.__file = file
        self.__xmltree = ''
        self.__root = ''
        self.parseConfig()

    def parseConfig(self):
        """Parse the xml-file from __init__."""
        self.__xmltree = xml.etree.ElementTree.parse(self.__file)
        self.__root = self.__xmltree.getroot()

    def getCustomerTokens(self):
        """
        Return the constomer_token and the customer_secret.

        :return:
        """
        token = []
        token['consumer_key'] = self.__root.get('consumer_key')
        token['consumer_secret'] = self.__root.get('consumer_secret')
        return token

    def setCustomerTokens(self, ck, cs):
        """
        Set the constomer_token and the customer_secret.

        param ck: customer key
        param cs: cistomer secret
        """
        self.__root.set('consumer_key', ck)
        self.__root.set('consumer_secret', cs)

    def getBots(self):
        """
        Return the propertys of all bots.

        :param botname:
        :return:
        """
        botProp = {}
        for child in self.__root.iter('bot'):
            botProp['id'] = child.get('id')
            botProp['object'] = child.find('object').text
        return botProp

    def addBot(self, id, object):
        """
        Add a bot to the config.

        :param id:
        :param object:
        """
        pickleString = pickle.dumps(object)
        exists = False
        for bot in self.__root.iter('bot'):
            if bot.get('id') == id:
                bot.find('object').text = pickleString
                exists = True
        if not exists:
            botAttrib = {}
            botAttrib['id'] = id
            botRoot = xml.etree.ElementTree.Element('bot', botAttrib)
            xml.etree.ElementTree.SubElement(botRoot, 'object')
            botRoot.find('object').text = pickleString
            self.__root.append(botRoot)

    def writeConfig(self):
        """Write the config-tree to the config-file from __init__."""
        self.__xmltree.write(self.__file, 'UTF-8')

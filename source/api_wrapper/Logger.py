import datetime
from pathlib import Path


class Logger:
    def __init__(self):
        self.__logging = False
        self.__logFile = ''

    def activate(self, path, name, overwrite_sensitive=True):
        """
        Activate the action log. Required are a path and a name for the log file.
        It's sensitive for overwriting files and stops if a specified file already exists.
        :param path:
        :param name:
        :param overwrite_sensitive:
        :return:
        """

        if path == '':
            raise Exception('Missing path for the logging file')
        elif name == '':
            raise Exception('Missing name for logging file')

        f = Path(path)

        if not f.is_dir():
            raise Exception('The directory "' + path + '" does not exist')

        log_file_path = path + '/' + name + '.txt'
        f = Path(log_file_path)

        if f.exists() and overwrite_sensitive:
            raise Exception('The logging file already exists')

        self.__logging = True
        self.__logFile = path + '/' + name + '.txt'

        file = open(self.__logFile, 'a')
        file.write('Log File for SocialBot created on ' + str(datetime.datetime.now()).split('.')[0] + '\n')
        file.write('####' + '\n')
        file.close()

    def log(self, message):
        """
        Logs a message if a log file was specified with activate_log.
        It can handle a simple string or a dict as message object.
        If message is a dict the key and the content are written to the log file.
        Every log to the log file contains a datestamp.
        :param message:
        :return:
        """

        if self.__logging and self.__logFile != '':
            if isinstance(message, str):
                f = open(self.__logFile, 'a')
                f.write(str(datetime.datetime.now()).split('.')[0] + ' | ' + message + '\n')
                f.write('####' + '\n')
                f.close()

            elif isinstance(message, dict):
                f = open(self.__logFile, 'a')
                f.write(str(datetime.datetime.now()).split('.')[0] + ': ' + '\n')
                keys = message.keys()

                for key in keys:
                    f.write(key + ': ' + message[key] + '\n')

                f.write('####' + '\n')
                f.close()

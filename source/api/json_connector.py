import json
import os


class JSONConnector:

    @staticmethod
    def set_json_file_content(directory, name, data):
        if directory[-1:] != '/':
            directory += '/'
        elif '.' in name:
            raise ValueError('Name should not contain a file type.', name)

        if not data:
            raise ValueError('Missing data to write to json file.')

        file_path = directory + name + '.json'

        if os.path.isfile(file_path):
            os.remove(file_path)

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file)

    @staticmethod
    def get_json_file_content(directory, name):
        if directory[:-1] != '/':
            directory += '/'
        elif '.' in name:
            raise ValueError('Name should not contain a file type.', name)

        file_path = directory + name + '.json'

        if os.path.isfile(file_path):
            with open(file_path, 'r') as json_file:
                return json.load(json_file)
        else:
            return


import json


class APIMessage:
    @staticmethod
    def create(message=None, code=None, dump=None):
        mes = {}

        if message:
            mes['message'] = message
        if code:
            mes['code'] = code
        if dump:
            mes['dump'] = dump

        return json.dumps(mes)

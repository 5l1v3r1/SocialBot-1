import json


class APIError:
    @staticmethod
    def create(message=None, code=None, dump=None):
        error = {}

        if message:
            error['error'] = message
        if code:
            error['code'] = code
        if dump:
            error['dump'] = dump

        return json.dumps(error)

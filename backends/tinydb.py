from tinydb import TinyDB

from .backend import Backend


class TinyDBBackend(Backend):
    def __init__(self, filename='db.json'):
        self.db = TinyDB(filename)

    def write(self, status):
        self.db.insert({
            'created_at': str(status.created_at),
            'user': status.user.screen_name,
            'text': status.text
        })

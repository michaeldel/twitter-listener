import requests

from .backend import Backend


class DiscordWebhookBackend(Backend):
    def __init__(self, endpoint='https://127.0.0.1', important=False):
        self.endpoint = endpoint

    def write(self, status):
        name = status.user.screen_name
        url = f'https://twitter.com/{name}/status/{status.id}'
        requests.post(self.endpoint, data={
            'content': f"_@{name}_ just twitted: {url}"
        })

from app.interfaces import IColorMindRepo
from app.types import pallets
import requests


class ColorMindRepo(IColorMindRepo):

    def __init__(self):
        self.base_url = 'http://colormind.io'

    def random(self, model: str) -> pallets:
        payload = {'model': model}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = "{}/api/".format(self.base_url)
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        resp = r.json()
        print(resp)
        if 'result' in resp:
            return resp['result']
        return []

    def suggest(self, model: str, colors: pallets) -> pallets:
        payload = {'model': model, 'input': colors}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = "{}/api/".format(self.base_url)
        r = requests.post(url, json=payload, headers=headers)
        resp = r.json()
        if 'result' in resp:
            return resp['result']
        return []

    def models(self) -> list[str]:
        url = "{}/list".format(self.base_url)
        r = requests.get(url)
        resp = r.json()
        if 'result' in resp:
            return resp['result']
        return []

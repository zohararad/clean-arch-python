from .interfaces import IColorMindRepo, pallets
from typing import Union


class ColorMindSvc(object):

    def __init__(self, repo: IColorMindRepo):
        self.repo = repo

    def random(self, model: str) -> Union[pallets, Exception]:
        try:
            return self.repo.random(model)
        except Exception as e:
            return e

    def suggest(self, model: str, colors: pallets) -> Union[pallets, Exception]:
        try:
            return self.repo.suggest(model, colors)
        except Exception as e:
            return e

    def models(self) -> Union[list[str], Exception]:
        try:
            return self.repo.models()
        except Exception as e:
            return e

from .types import pallets, IfaceException


class IColorMindRepo(object):

    def random(self, model: str) -> pallets:
        raise IfaceException("random should be implemented")

    def suggest(self, model: str, colors: pallets) -> pallets:
        raise IfaceException("suggest should be implemented")

    def models(self) -> list[str]:
        raise IfaceException("models should be implemented")


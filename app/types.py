from typing import Union


pallet = list[Union[int, str]]
pallets = list[pallet]


class IfaceException(Exception):
    pass



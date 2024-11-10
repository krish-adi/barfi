from typing import Union
from dataclasses import dataclass

BlockInterfaceValue = Union[int, float, str, None, bool]


@dataclass
class BlockInterface:
    name: str
    value: BlockInterfaceValue = None
    id: str = None

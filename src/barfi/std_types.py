from typing import Union, List, Optional
from dataclasses import dataclass, field

Value = Union[int, float, str, None, bool]


@dataclass
class BlockOption:
    name: str
    type: str
    value: Optional[Union[bool, str, int, float]] = None
    min: Optional[Union[int, float]] = None
    max: Optional[Union[int, float]] = None
    items: List[str] = field(default_factory=list)
    properties: dict = field(default_factory=dict)


@dataclass
class BlockInterface:
    name: str
    value: Value = None
    id: str = None

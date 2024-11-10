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


@dataclass
class FlowNodePosition:
    x: float
    y: float


@dataclass
class FlowNodeMeasured:
    width: int
    height: int


@dataclass
class FlowNode:
    id: str
    type: str
    name: str
    inputs: List[List[Optional[str]]]
    outputs: List[List[Optional[str]]]
    options: List
    position: FlowNodePosition
    measured: FlowNodeMeasured


@dataclass
class FlowConnection:
    id: str
    source: str
    target: str
    sourceHandle: str
    targetHandle: str


@dataclass
class FlowViewport:
    x: float
    y: float
    zoom: float


@dataclass
class FlowEditorState:
    nodes: List[FlowNode]
    connections: List[FlowConnection]
    viewport: FlowViewport


@dataclass
class BarfiResponse:
    command: str
    editor_state: FlowEditorState

from typing import List, Optional
from dataclasses import dataclass


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

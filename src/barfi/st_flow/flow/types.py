from typing import List, Tuple, Union, Literal
from dataclasses import dataclass
from barfi.config import SCHEMA_VERSION

NodeOptionValue = Union[int, float, str, None, bool]
NodeInterfaceValue = Union[int, float, str, None, bool]


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
    inputs: List[Tuple[str, NodeInterfaceValue]]
    outputs: List[Tuple[str, NodeInterfaceValue]]
    options: List[Tuple[str, NodeOptionValue]]
    position: FlowNodePosition
    measured: FlowNodeMeasured


@dataclass
class FlowConnection:
    id: str
    outputNode: str
    outputNodeInterface: str
    inputNode: str
    inputNodeInterface: str


@dataclass
class FlowViewport:
    x: float
    y: float
    zoom: float


@dataclass
class FlowEditorState:
    version: str
    nodes: List[FlowNode]
    connections: List[FlowConnection]
    viewport: FlowViewport


@dataclass
class StreamlitFlowResponse:
    command: Union[str, Literal["default", "execute", "save"]]
    editor_state: FlowEditorState


def build_streamlit_flow_response(_from_client: dict) -> StreamlitFlowResponse:
    if _from_client["command"] == "default":
        return StreamlitFlowResponse(
            command=_from_client["command"],
            editor_state=FlowEditorState(
                version=SCHEMA_VERSION,
                nodes=[],
                connections=[],
                viewport=FlowViewport(0, 0, 1),
            ),
        )
    else:
        return StreamlitFlowResponse(
            command=_from_client["command"],
            editor_state=FlowEditorState(
                version=SCHEMA_VERSION,
                nodes=[
                    FlowNode(**node) for node in _from_client["editor_state"]["nodes"]
                ],
                connections=[
                    FlowConnection(**conn)
                    for conn in _from_client["editor_state"]["connections"]
                ],
                viewport=FlowViewport(**_from_client["editor_state"]["viewport"]),
            ),
        )

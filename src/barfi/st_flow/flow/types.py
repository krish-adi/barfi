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
class FlowSchema:
    version: str
    nodes: List[FlowNode]
    connections: List[FlowConnection]
    viewport: FlowViewport


@dataclass
class StreamlitFlowResponse:
    command: Union[str, Literal["default", "execute", "save"]]
    editor_schema: FlowSchema


def build_flow_schema_from_dict(schema_dict: dict) -> FlowSchema:
    return FlowSchema(
        version=schema_dict.get("version", SCHEMA_VERSION),
        nodes=[
            FlowNode(
                **{
                    **node,
                    "position": FlowNodePosition(**node["position"]),
                    "measured": FlowNodeMeasured(**node["measured"]),
                }
            )
            for node in schema_dict.get("nodes", {})
        ],
        connections=[
            FlowConnection(**conn) for conn in schema_dict.get("connections", {})
        ],
        viewport=FlowViewport(**schema_dict.get("viewport", {})),
    )


def build_streamlit_flow_response(_from_client: dict) -> StreamlitFlowResponse:
    if _from_client["command"] == "default":
        return StreamlitFlowResponse(
            command=_from_client["command"],
            editor_schema=FlowSchema(
                version=SCHEMA_VERSION,
                nodes=[],
                connections=[],
                viewport=FlowViewport(0, 0, 1),
            ),
        )
    else:
        return StreamlitFlowResponse(
            command=_from_client["command"],
            editor_schema=build_flow_schema_from_dict(_from_client["editor_state"]),
        )

from typing import List, Tuple, Union, Literal
from dataclasses import dataclass
from barfi.config import SCHEMA_VERSION

NodeOptionValue = Union[int, float, str, None, bool]
NodeInterfaceValue = Union[int, float, str, None, bool]


@dataclass
class FlowNodePosition:
    """Represents the position of a node in the flow editor.

    Attributes:
        x (float): X-coordinate position of the node
        y (float): Y-coordinate position of the node
    """

    x: float
    y: float


@dataclass
class FlowNodeMeasured:
    """Represents the dimensions of a node in the flow editor.

    Attributes:
        width (int): Width of the node in pixels
        height (int): Height of the node in pixels
    """

    width: int
    height: int


@dataclass
class FlowNode:
    """Represents a node in the flow editor with its complete configuration.

    Attributes:
        id (str): Unique identifier for the node
        type (str): Type of the node, this is the name of the block dereived from the base blocks
        name (str): Display name of the node, a label for identyfing the node by a string
        inputs (List[Tuple[str, NodeInterfaceValue]]): List of input interfaces as (name, value) pairs
        outputs (List[Tuple[str, NodeInterfaceValue]]): List of output interfaces as (name, value) pairs
        options (List[Tuple[str, NodeOptionValue]]): List of node options as (name, value) pairs
        position (FlowNodePosition): Position of the node in the editor
        measured (FlowNodeMeasured): Dimensions of the node
    """

    id: str
    type: str
    name: str
    label: str
    inputs: List[Tuple[str, NodeInterfaceValue]]
    outputs: List[Tuple[str, NodeInterfaceValue]]
    options: List[Tuple[str, NodeOptionValue]]
    position: FlowNodePosition
    measured: FlowNodeMeasured


@dataclass
class FlowConnection:
    """Represents a connection between two nodes in the flow editor.

    Attributes:
        id (str): Unique identifier for the connection
        outputNode (str): ID of the node where the connection starts
        outputNodeInterface (str): Name of the output interface on the source node
        inputNode (str): ID of the node where the connection ends
        inputNodeInterface (str): Name of the input interface on the target node
    """

    id: str
    outputNode: str
    outputNodeInterface: str
    inputNode: str
    inputNodeInterface: str


@dataclass
class FlowViewport:
    """Represents the current view state of the flow editor.

    Attributes:
        x (float): X-coordinate of the viewport position
        y (float): Y-coordinate of the viewport position
        zoom (float): Current zoom level of the viewport
    """

    x: float
    y: float
    zoom: float


@dataclass
class FlowSchema:
    """Represents the complete schema of a flow diagram.

    Attributes:
        version (str): Schema version identifier
        nodes (List[FlowNode]): List of all nodes in the flow
        connections (List[FlowConnection]): List of all connections between nodes
        viewport (FlowViewport): Current state of the editor viewport
    """

    version: str
    nodes: List[FlowNode]
    connections: List[FlowConnection]
    viewport: FlowViewport


@dataclass
class StreamlitFlowResponse:
    """Represents the response structure for Streamlit flow operations.

    Attributes:
        command (Union[str, Literal["default", "execute", "save"]]): The command to be executed
        editor_schema (FlowSchema): The complete flow editor schema
    """

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
    return StreamlitFlowResponse(
        command=_from_client["command"],
        editor_schema=build_flow_schema_from_dict(_from_client["editor_schema"]),
    )

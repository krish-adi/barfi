from typing import List, Union, Dict
from dataclasses import dataclass, field, asdict
from barfi.config import SCHEMA_VERSION
from barfi.flow.block import Block

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
class FlowNodeInterface:
    name: str
    itype: str


@dataclass
class FlowNodeOption:
    name: str
    value: NodeOptionValue


@dataclass
class FlowNode:
    """Represents a node in the flow editor with its complete configuration.

    Attributes:
        id (str): Unique identifier for the node
        type (str): Type of the node, this is the name of the block dereived from the base blocks
        name (str): Display name of the node, a label for identyfing the node by a string
        inputs (List[FlowNodeInterface]): List of input interfaces with name and valueType
        outputs (List[FlowNodeInterface]): List of output interfaces with name and valueType
        options (List[FlowNodeOption]): List of node options with name and value
        position (FlowNodePosition): Position of the node in the editor
        measured (FlowNodeMeasured): Dimensions of the node
    """

    id: str
    type: str
    name: str
    label: str
    inputs: List[FlowNodeInterface]
    outputs: List[FlowNodeInterface]
    options: List[FlowNodeOption]
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

    _block_map: Dict[str, Block] = field(
        init=False,
        default_factory=dict,
        repr=False,
        compare=False,
        metadata={"export": False},
    )

    def block(
        self, node: FlowNode = None, node_id: str = None, node_label: str = None
    ) -> Block:
        """
        Creates or retrieves a Block instance from a FlowNode or node identifiers.

        Args:
            node (FlowNode, optional): FlowNode instance to create block from. Defaults to None.
            node_id (str, optional): Unique identifier for the node. Defaults to None.
            node_label (str, optional): Display label for the node. Defaults to None.

        Returns:
            Block: A Block instance representing the node in the flow.

        Example:
            >>> block = flow_schema.block(node_label="Result-1")
        """

        if node:
            node_id = node.id
            node_label = node.label

        if node_label:
            node_id = next((n.id for n in self.nodes if n.label == node_label), None)

        if node_id is None or node_id not in self._block_map:
            raise ValueError(
                "Could not find block: no valid node ID, node, or label was provided"
            )  # noqa

        return self._block_map[node_id]

    def export(self) -> dict:
        """
        Convert the dataclass to a dictionary, excluding fields marked with metadata `export=False`.
        """
        return {
            key: value
            for key, value in asdict(self).items()
            if self.__dataclass_fields__[key].metadata.get("export", True)
        }


def build_flow_schema_from_dict(schema_dict: dict) -> FlowSchema:
    # TODO move this to a classmethod of FlowSchema import()
    return FlowSchema(
        version=schema_dict.get("version", SCHEMA_VERSION),
        nodes=[
            FlowNode(
                **{
                    **node,
                    "inputs": [FlowNodeInterface(**input) for input in node["inputs"]],
                    "outputs": [
                        FlowNodeInterface(**output) for output in node["outputs"]
                    ],
                    "options": [FlowNodeOption(**option) for option in node["options"]],
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

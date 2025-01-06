from typing import Union, Literal
from dataclasses import dataclass
from barfi.flow.schema.types import FlowSchema, build_flow_schema_from_dict


@dataclass
class StreamlitFlowResponse:
    """Represents the response structure for Streamlit widget st_flow.

    Attributes:
        command (Union[str, Literal["default", "execute", "save"]]): The command to be executed
        editor_schema (FlowSchema): The complete flow editor schema
    """

    command: Union[str, Literal["default", "execute", "save"]]
    editor_schema: FlowSchema


def build_streamlit_flow_response(_from_client: dict) -> StreamlitFlowResponse:
    # TODO move this to a classmethod of StreamlitFlowResponse import()
    return StreamlitFlowResponse(
        command=_from_client["command"],
        editor_schema=build_flow_schema_from_dict(_from_client["editor_schema"]),
    )

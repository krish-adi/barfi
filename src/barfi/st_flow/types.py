from barfi.st_flow.flow.types import FlowEditorState
from dataclasses import dataclass


@dataclass
class BarfiResponse:
    command: str
    editor_state: FlowEditorState

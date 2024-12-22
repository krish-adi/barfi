from typing import List
from barfi.st_flow.block import Block
from barfi.st_flow.flow.types import FlowSchema


class ComputeEngine:
    def __init__(self, schema: FlowSchema, blocks: List[Block]):
        self._schema = schema
        self._blocks = blocks

    def compute(self):
        pass

import copy as copy
from barfi.st_flow.block import Block
from typing import List, Dict


class ComputeEngine(object):
    def __init__(self, **kwargs) -> None:
        # The primitive block types that are tied to this compute engine
        self._blocks: List[Block] = []

        # The state of the editor that is stored as JSON/Dict that represents
        # the active blocks and links on the editor
        self._editor_state = {}

        # Active blocks extracted from the editor_state.
        self._active_blocks = {}

        # Mapping all the active blocks and connections to their id and names
        # self._map = {}

        # Create a directed-acyclic-graph of the blocks and links
        # The computational graph
        self._graph = {}

        # Result from the execution for the compute engine
        self._result = {}

    @classmethod
    def create(cls, blocks: List[Block] = []):
        # classmethod to create a compute engine that extracts the information of
        # the given set of blocks, sets the self._blocks parameter and returns the
        # Compoute engine objects
        # Initialise the Compute Enginge
        # The primitive block types that are tied to this compute engine
        cls._blocks: List[Block] = blocks
        pass

    @classmethod
    def build_graph(cls, flow_state):
        # classmethod that uses the block state initialized in the above method
        # create() and builds a flow graph and returns the newly created method 
        # with the graph. this makes it easy with flow editor states that have 
        # multiple roots to return a list of graphs to be executed. 
        # this could possible also improve parallel execution on multiple branches 
        # at each level
        pass

    def add_editor_state(self, editor_state):
        self._editor_state = editor_state

    def get_result(self) -> Dict:
        # return self._active_blocks
        return self._result

    def execute(self):
        # Execute the flow by going through the graph that was created on the
        # flow with connections and the blocks
        pass

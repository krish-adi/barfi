import asyncio
from copy import deepcopy
from typing import List, Union, Dict, Tuple
from barfi.flow.block import Block
from barfi.flow.schema.types import FlowSchema


class ComputeEngine:
    def __init__(self, blocks: Union[List[Block], Dict[str, List[Block]]]):
        self._blocks = blocks

    def _make_map_node_block(self, schema: FlowSchema) -> Dict[str, Block]:
        """
        Creates a mapping between node IDs and Block instances based on a flow schema.

        Args:
            schema (FlowSchema): The flow schema containing nodes to be mapped.

        Returns:
            Dict[str, Block]: A dictionary mapping node IDs to corresponding Block instances.
            Each Block instance is a deep copy of the original block template.

        The method first creates a mapping of block names to block templates from self._blocks,
        which can be either a List of blocks or a Dict of categorized blocks.
        Then it creates a new mapping of node IDs to Block instances for nodes in the schema
        that have corresponding block templates.
        """

        _map_name_block = {}
        if isinstance(self._blocks, List):
            for block in self._blocks:
                _map_name_block[block.name] = block
        elif isinstance(self._blocks, Dict):
            for category, blocks in self._blocks.items():
                for block in blocks:
                    _map_name_block[block.name] = block

        _map_node_block: Dict[str, Block] = {}
        for node in schema.nodes:
            if node.name in _map_name_block:
                _node_block: Block = deepcopy(_map_name_block[node.name])
                for _opt in node.options:
                    # TODO: ideally to be _opt.name, _opt.type, _opt.value
                    _node_block.set_option(_opt.name, value=_opt.value)

                _map_node_block[node.id] = _node_block

        return _map_node_block

    def _make_execution_graph(
        self, schema: FlowSchema
    ) -> Tuple[Dict[str, List[str]], List[str]]:
        """
        Creates a directed graph representation of the flow schema.

        Args:
            schema (FlowSchema): The flow schema containing nodes and connections

        Returns:
            Tuple[Dict[str, List[str]], List[str]]: A tuple containing:
                - Dict[str, List[str]]: A dictionary where keys are node IDs and values are
                lists of child node IDs that they connect to
                - List[str]: A list of root node IDs (nodes with no incoming connections)
        """
        # Create adjacency list representation
        graph = {node.id: [] for node in schema.nodes}

        # Track incoming connections to identify root nodes
        has_incoming = set()

        # Build the graph connections
        for conn in schema.connections:
            from_node = conn.outputNode
            to_node = conn.inputNode
            graph[from_node].append(to_node)
            has_incoming.add(to_node)

        # Find root nodes (nodes with no incoming connections)
        root_nodes = [
            node_id for node_id in graph.keys() if node_id not in has_incoming
        ]

        return graph, root_nodes

    def _traverse_graph_compute_blocks(
        self, graph: Dict[str, List[str]], root_nodes: List[str]
    ):
        """
        Generator that traverses the execution graph from root nodes in topological order.

        Args:
            graph (Dict[str, List[str]]): Adjacency list representation of the graph
            root_nodes (List[str]): List of nodes with no incoming edges

        Yields:
            str: Node ID in execution order
        """
        visited = set()
        queue = root_nodes.copy()

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                yield current

                # Add child nodes to queue
                for child in graph[current]:
                    # Only add child if all its parents have been visited
                    parents_visited = all(
                        parent not in graph or parent in visited
                        for parent in graph.keys()
                        if child in graph[parent]
                    )
                    if parents_visited and child not in queue:
                        queue.append(child)

    @staticmethod
    def _propagate_interface_values(
        schema: FlowSchema, node_id: str, _map_node_block: Dict[str, Block]
    ):
        """
        Propagates output values from a node to its connected input interfaces.

        Args:
            schema (FlowSchema): The flow schema containing connections
            node_id (str): ID of the node whose outputs need to be propagated
            _map_node_block (Dict[str, Block]): Mapping of node IDs to Block instances
        """
        for conn in schema.connections:
            if conn.outputNode == node_id:
                input_node_block = _map_node_block[conn.inputNode]
                input_node_block.set_interface(
                    conn.inputNodeInterface,
                    _map_node_block[node_id].get_interface(conn.outputNodeInterface),
                )

    def execute(self, schema: FlowSchema):
        """
        Executes the flow schema synchronously by processing blocks in topological order.

        This method creates a mapping of nodes to blocks, builds an execution graph,
        and processes each block in the correct order. For each block, it:
        1. Runs the block's compute function synchronously
        2. Propagates output values to connected blocks
        3. Updates the schema with the final block mapping

        Args:
            schema (FlowSchema): The flow schema to execute, containing nodes and their connections

        Note:
            This method handles async blocks by running them in a synchronous context using asyncio.run()
        """
        _map_node_block = self._make_map_node_block(schema)
        _execution_graph, _root_nodes = self._make_execution_graph(schema)

        # Traverse the graph and compute the blocks
        for node_id in self._traverse_graph_compute_blocks(
            _execution_graph, _root_nodes
        ):
            block = _map_node_block[node_id]
            # Run async computation in synchronous context
            asyncio.run(block._on_compute())
            self._propagate_interface_values(schema, node_id, _map_node_block)

        schema._block_map = _map_node_block

    async def async_execute(self, schema: FlowSchema):
        """
        Executes the flow schema asynchronously by processing blocks in topological order.

        This method creates a mapping of nodes to blocks, builds an execution graph,
        and processes each block in the correct order. For each block, it:
        1. Awaits the block's compute function
        2. Propagates output values to connected blocks
        3. Updates the schema with the final block mapping

        Args:
            schema (FlowSchema): The flow schema to execute, containing nodes and their connections

        Note:
            This method should be called with await when executing async blocks
        """
        _map_node_block = self._make_map_node_block(schema)
        _execution_graph, _root_nodes = self._make_execution_graph(schema)

        # Traverse the graph and compute the blocks
        for node_id in self._traverse_graph_compute_blocks(
            _execution_graph, _root_nodes
        ):
            block = _map_node_block[node_id]
            await block._on_compute()  # await the async compute function
            self._propagate_interface_values(schema, node_id, _map_node_block)

        schema._block_map = _map_node_block

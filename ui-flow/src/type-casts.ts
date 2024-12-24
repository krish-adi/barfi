import { Edge, Node } from "@xyflow/react";
import { FlowStateConnection, FlowStateNode, BaseBlock } from "./types";

export function convertFlowConnectionsToEdges(
    connections: FlowStateConnection[]
): Edge[] {
    return connections.map((conn) => ({
        id: conn.id,
        source: conn.outputNode,
        sourceHandle: conn.outputNodeInterface,
        target: conn.inputNode,
        targetHandle: conn.inputNodeInterface,
    }));
}

export function convertFlowNodesToNodes(
    nodes: FlowStateNode[],
    baseBlocks: BaseBlock[] | Record<string, BaseBlock[]>
): Node[] {
    return nodes.map((_node) => {
        const allBaseBlocks = Array.isArray(baseBlocks)
            ? baseBlocks
            : Object.values(baseBlocks).flat();

        const baseBlock = {
            ...allBaseBlocks.find((bb) => bb.name === _node.type),
        };
        return {
            id: _node.id,
            type: "baseBlock",
            data: {
                blockData: {
                    name: _node.type,
                    type: _node.type,
                    label: _node.label,
                    inputs: _node.inputs.map((input) => ({
                        name: input.name,
                        itype: input.itype,
                    })),
                    outputs: _node.outputs.map((output) => ({
                        name: output.name,
                        itype: output.itype,
                    })),
                    options: _node.options.map((option) => {
                        const baseOption = baseBlock.options?.find(
                            (opt) => opt.name === option.name
                        );
                        return {
                            ...baseOption,
                            name: option.name,
                            value: option.value,
                        };
                    }),
                } as BaseBlock,
            },
            position: _node.position,
            measured: _node.measured,
        };
    });
}

import { useReactFlow, Node, Edge, Viewport } from "@xyflow/react";
import { useNodeDataStore } from "@/components/nodes/nodeStore";
import {
    BaseBlock,
    BlockOption,
    FlowStateNode,
    FlowStateEdge,
} from "@/types";

function constructFlowState(
    nodes: Node[],
    edges: Edge[],
    viewport: Viewport,
    nodesOptionData: Record<string, Record<string, BlockOption>>
) {
    console.log(nodes);
    console.log(edges);
    console.log(nodesOptionData);
    // const flowState = [];
    const flowStateNodes: FlowStateNode[] = nodes.map((node) => {
        const blockData = node.data.blockData as BaseBlock;
        return {
            id: node.id,
            type: blockData.name,
            name: blockData.label,
            options: blockData.options.map((option) => [
                option.name,
                nodesOptionData[node.id][option.name].value,
            ]),
            interfaces: [
                ...blockData.inputs.map((input) => {
                    return [
                        input.name,
                        {
                            id: `${node.id}__${input.name}`,
                            value: null,
                        },
                    ];
                }),
                ...blockData.outputs.map((output) => {
                    return [
                        output.name,
                        {
                            id: `${node.id}__${output.name}`,
                            value: null,
                        },
                    ];
                }),
            ],
            position: node.position,
            measured: node.measured,
        };
    });
    const flowStateEdges: FlowStateEdge[] = edges.map((edge) => {
        return {
            id: edge.id,
            from: `${edge.source}__${edge.sourceHandle}`,
            to: `${edge.target}__${edge.targetHandle}`,
            source: edge.source,
            target: edge.target,
            sourceHandle: edge.sourceHandle,
            targetHandle: edge.targetHandle,
        };
    });
    return {
        nodes: flowStateNodes,
        edges: flowStateEdges,
        connections: flowStateEdges,
        viewport: viewport,
    };
}

export default function PanelRun({
    onClickRun,
}: {
    onClickRun: ({
        command,
        editor_state,
    }: {
        command: string;
        editor_state: {
            nodes: FlowStateNode[];
            edges: FlowStateEdge[];
            connections: FlowStateEdge[];
            viewport: Viewport;
        };
    }) => void;
}) {
    const { getNodes, getEdges, getViewport } = useReactFlow();
    const getNodesOptionDataFromStore = useNodeDataStore(
        (state) => state.getNodesOptionData
    );
    return (
        <button
            className="border rounded-sm border-black px-2 py-0.5"
            onClick={() => {
                onClickRun({
                    command: "execute",
                    editor_state: constructFlowState(
                        getNodes(),
                        getEdges(),
                        getViewport(),
                        getNodesOptionDataFromStore()
                    ),
                });
            }}
        >
            Run <span className="ml-2">🚀</span>{" "}
        </button>
    );
}

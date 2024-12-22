import { useReactFlow, Node, Edge, Viewport } from "@xyflow/react";
import { useFlowStateStore } from "@/components/flow/flow-state";
import {
    BaseBlock,
    BlockOption,
    FlowStateNode,
    FlowStateConnection,
} from "@/types";
import { TriangleRightIcon } from "@radix-ui/react-icons";

function constructFlowState(
    nodes: Node[],
    edges: Edge[],
    viewport: Viewport,
    nodesOptionData: Record<string, Record<string, BlockOption>>
) {
    const flowStateNodes: FlowStateNode[] = nodes.map((node) => {
        const blockData = node.data.blockData as BaseBlock;
        return {
            id: node.id,
            name: blockData.name,
            type: blockData.type,
            label: blockData.label || "",
            inputs: blockData.inputs.map((input) => ({
                name: input.name,
                value: input.value,
            })),
            outputs: blockData.outputs.map((output) => ({
                name: output.name,
                value: output.value,
            })),
            options: blockData.options.map((option) => ({
                name: option.name,
                value: nodesOptionData[node.id][option.name].value,
            })),
            position: node.position,
            measured: node.measured || { width: 0, height: 0 },
        };
    });
    const flowStateConnections: FlowStateConnection[] = edges.map((edge) => {
        return {
            id: edge.id,
            outputNode: edge.source,
            outputNodeInterface: edge.sourceHandle ?? "",
            inputNode: edge.target,
            inputNodeInterface: edge.targetHandle ?? "",
        };
    });
    return {
        nodes: flowStateNodes,
        connections: flowStateConnections,
        viewport: viewport,
    };
}

export default function PanelRun({
    onClickRun,
}: {
    onClickRun: ({
        command,
        editor_schema,
    }: {
        command: string;
        editor_schema: {
            nodes: FlowStateNode[];
            connections: FlowStateConnection[];
            viewport: Viewport;
        };
    }) => void;
}) {
    const { getNodes, getEdges, getViewport } = useReactFlow();
    const getNodesOptionDataFromStore = useFlowStateStore(
        (state) => state.getNodesOptionData
    );
    return (
        <button
            className="flex items-center border rounded-sm border-black px-1 py-1 text-white bg-black"
            onClick={() => {
                onClickRun({
                    command: "execute",
                    editor_schema: constructFlowState(
                        getNodes(),
                        getEdges(),
                        getViewport(),
                        getNodesOptionDataFromStore()
                    ),
                });
            }}
        >
            <span className="ml-2">Execute</span>
            <span className="ml-1">
                <TriangleRightIcon className="w-6 h-6" />
            </span>
        </button>
    );
}

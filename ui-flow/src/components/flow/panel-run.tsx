import { useReactFlow, Node, Edge, Viewport } from "@xyflow/react";
import { useFlowStateStore } from "@/components/flow/flowState";
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
    console.log("nodes", nodes);
    console.log("edges", edges);
    console.log("node options", nodesOptionData);
    const flowStateNodes: FlowStateNode[] = nodes.map((node) => {
        const blockData = node.data.blockData as BaseBlock;
        return {
            id: node.id,
            type: blockData.name,
            name: blockData.label || "",
            inputs: blockData.inputs.map((input) => [input.name, null]),
            outputs: blockData.outputs.map((output) => [output.name, null]),
            options: blockData.options.map((option) => [
                option.name,
                nodesOptionData[node.id][option.name].value,
            ]),
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
        editor_state,
    }: {
        command: string;
        editor_state: {
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
                    editor_state: constructFlowState(
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

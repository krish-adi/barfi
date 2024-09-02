import { useReactFlow, Node, Edge, Viewport } from "@xyflow/react";
import { useNodeDataStore } from "@/components/nodes/nodeStore";
import {
    BaseBlock,
    BlockOption,
    FlowStateNode,
    FlowStateConnection,
} from "@/types";

function constructFlowStateOld(
    nodes: Node[],
    edges: Edge[],
    viewport: Viewport,
    nodesOptionData: Record<string, Record<string, BlockOption>>
) {
    console.log("nodes", nodes);
    console.log("edges", edges);
    console.log(nodesOptionData);
    // const flowState = [];
    const flowStateNodes: FlowStateNode[] = nodes.map((node) => {
        const blockData = node.data.blockData as BaseBlock;
        const inputInterfaces: [string, { id: string; value: null }][] = [];
        blockData.inputs.forEach((input) => {
            inputInterfaces.push([
                input.name,
                {
                    id: `${node.id}__${input.name}`,
                    value: null,
                },
            ]);
        });
        const outputInterfaces: [string, { id: string; value: null }][] = [];
        blockData.outputs.forEach((output) => {
            outputInterfaces.push([
                output.name,
                {
                    id: `${node.id}__${output.name}`,
                    value: null,
                },
            ]);
        });
        return {
            id: node.id,
            type: blockData.name,
            name: blockData.label || "",
            options: blockData.options.map((option) => [
                option.name,
                nodesOptionData[node.id][option.name].value,
            ]),
            interfaces: [...inputInterfaces, ...outputInterfaces],
            position: node.position,
            measured: node.measured || { width: 0, height: 0 },
        };
    });
    const flowStateConnections: FlowStateConnection[] = edges.map((edge) => {
        return {
            id: edge.id,
            from: `${edge.source}__${edge.sourceHandle ?? ""}`,
            to: `${edge.target}__${edge.targetHandle ?? ""}`,
            source: edge.source,
            target: edge.target,
            sourceHandle: edge.sourceHandle ?? "",
            targetHandle: edge.targetHandle ?? "",
        };
    });
    return {
        nodes: flowStateNodes,
        connections: flowStateConnections,
        viewport: viewport,
    };
}

function constructFlowState(
    nodes: Node[],
    edges: Edge[],
    viewport: Viewport,
    nodesOptionData: Record<string, Record<string, BlockOption>>
) {
    console.log("nodes", nodes);
    console.log("edges", edges);
    console.log(nodesOptionData);
    // const flowState = [];
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
            source: edge.source,
            target: edge.target,
            sourceHandle: edge.sourceHandle ?? "",
            targetHandle: edge.targetHandle ?? "",
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

import { useReactFlow, Node, Edge, Viewport } from "@xyflow/react";
import { useFlowStateStore } from "@/components/flow/flow-state";
import {
    BaseBlock,
    BlockOption,
    FlowStateNode,
    FlowStateConnection,
} from "@/types";
import { PlayIcon, StarIcon } from "@radix-ui/react-icons";

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
                itype: input.itype,
            })),
            outputs: blockData.outputs.map((output) => ({
                name: output.name,
                itype: output.itype,
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
        <div className="flex flex-row gap-2 text-sm text-white">
            <button
                className="flex items-center px-2 py-1 rounded-sm shadow-md bg-gray-600 gap-1"
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
                <span>
                    <PlayIcon className="w-3.5 h-3.5" />
                </span>
                <span>Execute</span>
            </button>
            <button
                className="flex items-center px-2 py-1 rounded-sm shadow-md bg-gray-600 gap-1"
                onClick={() => {
                    onClickRun({
                        command: "save",
                        editor_schema: constructFlowState(
                            getNodes(),
                            getEdges(),
                            getViewport(),
                            getNodesOptionDataFromStore()
                        ),
                    });
                }}
            >
                <span>
                    <StarIcon className="w-3.5 h-3.5" />
                </span>
                <span>Save</span>
            </button>
            {/* TODO: Not implemented to prevent clear of the complete editor by mistake */}
            {/* <button
                className="flex items-center px-2 py-1 rounded-sm shadow-md bg-gray-600 gap-1"
                onClick={() => {
                    console.log("first");
                }}
            >
                <span>
                    <ResetIcon className="w-3.5 h-3.5" />
                </span>
                <span>Reset</span>
            </button> */}
        </div>
    );
}

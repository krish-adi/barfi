import { useEffect } from "react";
import { withStreamlitConnection, Streamlit } from "streamlit-component-lib";
import { useNodesState, useEdgesState } from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import { useFlowStateStore } from "./components/flow/flow-state";
import { BarfiState, BaseBlock } from "@/types";
import FlowEditor from "./components/flow/flow-editor";
import {
    convertFlowNodesToNodes,
    convertFlowConnectionsToEdges,
} from "./type-casts";

export function App({ args }: { args: BarfiState }) {    
    const defaultNodes = convertFlowNodesToNodes(
        args.editor_schema.nodes,
        args.blocks
    );
    const defaultEdges = convertFlowConnectionsToEdges(
        args.editor_schema.connections
    );

    const addNodeToStore = useFlowStateStore((state) => state.addNode);
    const getNodesFromStore = useFlowStateStore((state) => state.getNodes);
    const setNodeBaseBlockCount = useFlowStateStore(
        (state) => state.setNodeBaseBlockCount
    );
    const nodeIDsInStore = Object.keys(getNodesFromStore());

    const [nodes, , onNodesChange] = useNodesState([...defaultNodes]);

    defaultNodes.forEach((node) => {
        if (!nodeIDsInStore.includes(node.id)) {
            addNodeToStore(node.id, node.data.blockData as BaseBlock);
            setNodeBaseBlockCount((node.data.blockData as BaseBlock).name);
        }
    });

    const [edges, setEdges, onEdgesChange] = useEdgesState([...defaultEdges]);

    useEffect(() => {
        Streamlit.setFrameHeight();
    }, [args]);

    return (
        <div className="border rounded-md w-full h-[36rem]">
            <FlowEditor
                nodes={nodes}
                edges={edges}
                setEdges={setEdges}
                onNodesChange={onNodesChange}
                onEdgesChange={onEdgesChange}
                baseBlocks={args.blocks}
            />
        </div>
    );
}

const StreamlitAppComponent = withStreamlitConnection(App);
export default StreamlitAppComponent;

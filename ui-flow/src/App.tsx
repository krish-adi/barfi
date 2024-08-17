import { useEffect, useCallback } from "react";
import { withStreamlitConnection, Streamlit } from "streamlit-component-lib";
import {
    ReactFlow,
    Background,
    useNodesState,
    useEdgesState,
    MiniMap,
    Controls,
    Panel,
    addEdge,
} from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import { initialEdges, initialNodes } from "./utils";

export function App({ args }) {
    // const { title, input_schema } = args;

    const proOptions = { hideAttribution: true };

    const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
    const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

    useEffect(() => {
        Streamlit.setFrameHeight();
    });

    const onClick = () => {
        console.log(args);
        // Streamlit.setComponentValue(values);
    };

    const onConnect = useCallback(
        (params) =>
            setEdges((els) => addEdge({ ...params, animated: true }, els)),
        []
    );

    const onPaneClick = useCallback((e) => {
        e.preventDefault();
        console.log(e);
    }, []);

    return (
        <>
            <div className="border rounded-md w-full h-[36rem]">
                <ReactFlow
                    nodes={nodes}
                    edges={edges}
                    onNodesChange={onNodesChange}
                    onEdgesChange={onEdgesChange}
                    onConnect={onConnect}
                    // onPaneClick={onPaneClick}
                    // onDoubleClick={onPaneClick}
                    onContextMenu={onPaneClick}
                    fitView={true}
                    proOptions={proOptions}
                    nodesDraggable
                    minZoom={0}
                >
                    <Background color="#aaa" gap={16} />
                    <MiniMap />
                    <Controls />
                    <Panel position="top-left">
                        <button className="" onClick={onClick}>
                            Run!
                        </button>
                    </Panel>
                </ReactFlow>
            </div>
        </>
    );
}

const StreamlitAppComponent = withStreamlitConnection(App);
export default StreamlitAppComponent;

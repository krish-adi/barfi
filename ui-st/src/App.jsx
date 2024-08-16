import { useEffect } from "react";
import { withStreamlitConnection, Streamlit } from "streamlit-component-lib";
import {
    ReactFlow,
    Background,
    MiniMap,
    Controls,
    Panel,
    NodeToolbar,
} from "@xyflow/react";

function App({ args }) {
    // const { title, input_schema } = args;

    const proOptions = { hideAttribution: true };

    const nodeStyle = {
        color: "#0041d0",
        borderColor: "#0041d0",
    };

    const nodes = [
        {
            type: "input",
            id: "1",
            data: { label: "Thanks" },
            position: { x: 100, y: 0 },
            style: nodeStyle,
            draggable: true,
        },
        {
            id: "2",
            data: { label: "for" },
            position: { x: 0, y: 100 },
            style: nodeStyle,
            draggable: true,
        },
        {
            id: "3",
            data: { label: "using" },
            position: { x: 200, y: 100 },
            style: nodeStyle,
            draggable: true,
        },
        {
            id: "4",
            data: { label: "React Flow Pro!" },
            position: { x: 100, y: 200 },
            style: nodeStyle,
            draggable: true,
        },
    ];

    const edges = [
        {
            id: "1->2",
            source: "1",
            target: "2",
            animated: true,
        },
        {
            id: "1->3",
            source: "1",
            target: "3",
            animated: true,
        },
        {
            id: "2->4",
            source: "2",
            target: "4",
            animated: true,
        },
        {
            id: "3->4",
            source: "3",
            target: "4",
            animated: true,
        },
    ];

    // const initialNodes = [
    //     { id: "1", position: { x: 0, y: 0 }, data: { label: "1" } },
    //     { id: "2", position: { x: 0, y: 100 }, data: { label: "2" } },
    // ];
    // const initialEdges = [{ id: "e1-2", source: "1", target: "2" }];

    useEffect(() => {
        Streamlit.setFrameHeight();
    });

    const onClick = () => {
        console.log(args);
        // Streamlit.setComponentValue(values);
    };

    return (
        <>
            <div className="border rounded-md w-full h-[36rem]">
                <ReactFlow
                    nodes={nodes}
                    edges={edges}
                    fitView={false}
                    proOptions={proOptions}
                    nodesDraggable
                >
                    <Background color="#aaa" gap={16} />
                    {/* <MiniMap nodeStrokeWidth={3} /> */}
                    <Controls />
                    <NodeToolbar />
                    <Panel position="top-left">top-left</Panel>
                </ReactFlow>
            </div>
            <button className="" onClick={onClick}>
                Run!
            </button>
        </>
    );
}

const StreamlitAppComponent = withStreamlitConnection(App);
export default StreamlitAppComponent;

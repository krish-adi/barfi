import { useEffect, useCallback } from "react";
import { withStreamlitConnection, Streamlit } from "streamlit-component-lib";
import { ContextMenu, ContextMenuTrigger } from "@/components/ui/context-menu";
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
import PanelContextMenuContent from "./components/flow/panel-context-menu-content";
import { initialEdges, initialNodes } from "./utils";

export function App({ args }) {
    // const { title, input_schema } = args;
    // const hiddenTriggerRef = useRef(null);

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

    // const onPanelContextClick = useCallback((e: React.MouseEvent) => {
    //     e.preventDefault();
    //     console.log(e);
    //     if (hiddenTriggerRef.current) {
    //         const contextMenuEvent = new MouseEvent("contextmenu", {
    //             bubbles: true,
    //             clientX: e.clientX,
    //             clientY: e.clientY,
    //         });
    //         (hiddenTriggerRef.current as HTMLElement).dispatchEvent(
    //             contextMenuEvent
    //         );
    //     }
    //     // // https://github.com/radix-ui/primitives/issues/1307
    //     // trigger.current.dispatchEvent(
    //     //     new MouseEvent("contextmenu", {
    //     //         bubbles: true,
    //     //         clientX: button.current.getBoundingClientRect().x,
    //     //         clientY: button.current.getBoundingClientRect().y,
    //     //     })
    //     // );
    // }, []);

    return (
        <div className="border rounded-md w-full h-[36rem]">
            <ContextMenu>
                <ContextMenuTrigger asChild>
                    {/* <div ref={hiddenTriggerRef} /> */}
                    <ReactFlow
                        nodes={nodes}
                        edges={edges}
                        onNodesChange={onNodesChange}
                        onEdgesChange={onEdgesChange}
                        onConnect={onConnect}
                        // onContextMenu={onPanelContextClick}
                        fitView={true}
                        proOptions={proOptions}
                        nodesDraggable
                        minZoom={0}
                    >
                        <Background color="#aaa" gap={16} />
                        <MiniMap position="top-right" />
                        <Controls />
                        <Panel position="bottom-right">
                            <button
                                className="border rounded-sm border-black px-2 py-0.5"
                                onClick={onClick}
                            >
                                Run <span className="ml-2">🚀</span>{" "}
                            </button>
                        </Panel>
                    </ReactFlow>
                </ContextMenuTrigger>
                <PanelContextMenuContent />
            </ContextMenu>
        </div>
    );
}

const StreamlitAppComponent = withStreamlitConnection(App);
export default StreamlitAppComponent;

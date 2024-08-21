import { useEffect, useCallback, useMemo } from "react";
import { withStreamlitConnection, Streamlit } from "streamlit-component-lib";
import { ContextMenu, ContextMenuTrigger } from "@/components/ui/context-menu";
import {
    ReactFlowProvider,
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
import PanelContextMenu from "./components/flow/panel-context-menu";
import PanelRun from "./components/flow/panel-run";
import nodeTypes from "./components/nodes";
import { useFlowUIStore } from "./components/flow/flowState";

export function App({ args }) {
    // const { title, input_schema } = args;
    // const hiddenTriggerRef = useRef(null);

    const proOptions = { hideAttribution: true };
    // const nodeTypes = useMemo(() => nodeTypes, []);

    const [nodes, setNodes, onNodesChange] = useNodesState([]);
    const [edges, setEdges, onEdgesChange] = useEdgesState([]);

    useEffect(() => {
        Streamlit.setFrameHeight();
    });

    const onConnect = useCallback(
        (params) =>
            setEdges((els) => addEdge({ ...params, animated: true }, els)),
        []
    );

    const setContextLocation = useFlowUIStore(
        (state) => state.setContextLocation
    );

    const onPanelContextClick = useCallback((e: React.MouseEvent) => {
        // e.preventDefault();
        // console.log(e);
        setContextLocation(e.clientX, e.clientY);
        // // https://github.com/radix-ui/primitives/issues/1307
        // if (hiddenTriggerRef.current) {
        //     const contextMenuEvent = new MouseEvent("contextmenu", {
        //         bubbles: true,
        //         clientX: e.clientX,
        //         clientY: e.clientY,
        //     });
        //     (hiddenTriggerRef.current as HTMLElement).dispatchEvent(
        //         contextMenuEvent
        //     );
        // }
    }, []);

    return (
        <div className="border rounded-md w-full h-[36rem]">
            <ReactFlowProvider>
                <ContextMenu>
                    <ContextMenuTrigger asChild>
                        {/* <div ref={hiddenTriggerRef} /> */}
                        <ReactFlow
                            nodeTypes={nodeTypes}
                            nodes={nodes}
                            edges={edges}
                            onNodesChange={onNodesChange}
                            onEdgesChange={onEdgesChange}
                            onConnect={onConnect}
                            onContextMenu={onPanelContextClick}
                            fitView={true}
                            fitViewOptions={{ padding: 0.75 }}
                            proOptions={proOptions}
                            nodesDraggable
                            minZoom={0}
                        >
                            <Background color="#aaa" gap={16} />
                            <MiniMap position="top-right" />
                            <Controls position="top-left" />
                            <Panel position="bottom-right">
                                <PanelRun />
                            </Panel>
                        </ReactFlow>
                    </ContextMenuTrigger>
                    <PanelContextMenu baseBlocks={args["base_blocks"]} />
                </ContextMenu>
            </ReactFlowProvider>
        </div>
    );
}

const StreamlitAppComponent = withStreamlitConnection(App);
export default StreamlitAppComponent;

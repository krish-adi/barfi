import { useEffect, useCallback } from "react";
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
import { BaseBlockNode } from "./components/nodes";
import { useFlowStateStore } from "./components/flow/flowState";
import { BarfiState } from "@/types";
import { v4 as uuid } from "uuid";

export function App({ args }: { args: BarfiState }) {
    const proOptions = { hideAttribution: true };

    const setContextLocation = useFlowStateStore(
        (state) => state.setContextLocation
    );
    const addNodeToStore = useFlowStateStore((state) => state.addNode);
    const getNodesFromStore = useFlowStateStore((state) => state.getNodes);
    const delNodeFromStore = useFlowStateStore((state) => state.delNode);
    const setNodeBaseBlockCount = useFlowStateStore(
        (state) => state.setNodeBaseBlockCount
    );
    const nodeIDsInStore = Object.keys(getNodesFromStore());

    const [nodes, , onNodesChange] = useNodesState([
        ...args.load_editor_schema.nodes,
    ]);

    args.load_editor_schema.nodes.forEach((node) => {
        if (!nodeIDsInStore.includes(node.id)) {
            addNodeToStore(node.id, node.data.blockData);
            setNodeBaseBlockCount(node.data.blockData.name);
        }
    });

    const [edges, setEdges, onEdgesChange] = useEdgesState([
        ...args.load_editor_schema.connections,
    ]);

    useEffect(() => {
        Streamlit.setFrameHeight();
    });

    const onConnect = useCallback(
        // @ts-expect-error params is not used
        (params) =>
            setEdges((eds) =>
                addEdge(
                    { ...params, animated: true, id: `edge__${uuid()}` },
                    eds
                )
            ),
        [setEdges]
    );

    // const hiddenTriggerRef = useRef(null);
    const onPanelContextClick = useCallback(
        (e: React.MouseEvent) => {
            setContextLocation(e.clientX, e.clientY);
            // e.preventDefault();
            // Keep this for future reference
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
        },
        [setContextLocation]
    );

    return (
        <div className="border rounded-md w-full h-[36rem]">
            <ReactFlowProvider>
                <ContextMenu>
                    <ContextMenuTrigger asChild>
                        {/* <div ref={hiddenTriggerRef} /> */}
                        <ReactFlow
                            nodeTypes={{ baseBlock: BaseBlockNode }}
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
                            onDelete={({ nodes }) => {
                                nodes.forEach((node) => {
                                    delNodeFromStore(node.id);
                                });
                            }}
                        >
                            <Background color="#aaa" gap={16} />
                            <MiniMap position="top-right" />
                            <Controls position="top-left" />
                            <Panel position="bottom-right">
                                <PanelRun
                                    onClickRun={Streamlit.setComponentValue}
                                />
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

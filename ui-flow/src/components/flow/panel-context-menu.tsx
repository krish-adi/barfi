import { memo } from "react";
import { v4 as uuid } from "uuid";
import {
    ContextMenuContent,
    ContextMenuItem,
    ContextMenuLabel,
    ContextMenuSeparator,
    // ContextMenuSub,
    // ContextMenuSubContent,
    // ContextMenuSubTrigger,
} from "@/components/ui/context-menu";
import { useReactFlow } from "@xyflow/react";
import { BaseBlock } from "@/types";
import { useFlowStateStore } from "@/components/flow/flowState";

function ContextMenuNodeItem({ blockData }: { blockData: BaseBlock }) {
    const { addNodes, screenToFlowPosition } = useReactFlow();
    const contextLocation = useFlowStateStore((state) => state.contextLocation);
    const setContextLocation = useFlowStateStore(
        (state) => state.setContextLocation
    );
    const addNodeToStore = useFlowStateStore((state) => state.addNode);
    const setNodeBaseBlockCount = useFlowStateStore(
        (state) => state.setNodeBaseBlockCount
    );
    return (
        <ContextMenuItem
            onClick={() => {
                // create a new block data with the label
                const newBlockData = {
                    ...blockData,
                    label: `${blockData.name} ${setNodeBaseBlockCount(
                        blockData.name
                    )}`,
                };

                const flowPos = screenToFlowPosition({
                    x: contextLocation.x || 0,
                    y: contextLocation.y || 0,
                });
                const nodeId = uuid();
                addNodes([
                    {
                        id: nodeId,
                        type: "baseBlock",
                        data: { blockData: newBlockData },
                        position: {
                            x: flowPos.x,
                            y: flowPos.y,
                        },
                    },
                ]);
                addNodeToStore(nodeId, blockData);
                setContextLocation(undefined, undefined);
            }}
        >
            {blockData.name}
        </ContextMenuItem>
    );
}

const PanelContextMenu = memo(({ baseBlocks }: { baseBlocks: BaseBlock[] }) => {
    // console.log(baseBlocks);
    return (
        <ContextMenuContent>
            <ContextMenuLabel>Add a node</ContextMenuLabel>
            <ContextMenuSeparator />
            {/* <ContextMenuSub>
                <ContextMenuSubTrigger>Node type 1</ContextMenuSubTrigger>
                <ContextMenuSubContent>
                    <ContextMenuItem>Node 1</ContextMenuItem>
                    <ContextMenuItem>Node 2</ContextMenuItem>
                    <ContextMenuItem>Node 3</ContextMenuItem>
                </ContextMenuSubContent>
            </ContextMenuSub> */}

            {baseBlocks.map((blockData) => (
                <ContextMenuNodeItem blockData={blockData} key={uuid()} />
            ))}
        </ContextMenuContent>
    );
});

export default PanelContextMenu;

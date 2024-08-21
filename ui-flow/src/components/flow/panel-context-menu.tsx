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
import { useFlowUIStore } from "./flowState";
import { BaseBlock } from "../../types";

function ContextMenuNodeItem({ blockData }: { blockData: BaseBlock }) {
    // console.log(blockData);
    const { addNodes, screenToFlowPosition } = useReactFlow();
    const contextLocation = useFlowUIStore((state) => state.contextLocation);
    const setContextLocation = useFlowUIStore(
        (state) => state.setContextLocation
    );
    return (
        <ContextMenuItem
            onClick={() => {
                const flowPos = screenToFlowPosition({
                    x: contextLocation.x || 0,
                    y: contextLocation.y || 0,
                });
                addNodes([
                    {
                        id: uuid(),
                        type: "custom",
                        data: { blockData },
                        position: {
                            x: flowPos.x,
                            y: flowPos.y,
                        },
                    },
                ]);
                setContextLocation(undefined, undefined);
            }}
        >
            {blockData.name}
        </ContextMenuItem>
    );
}

const PanelContextMenu = memo(({ baseBlocks }: { baseBlocks: BaseBlock[] }) => {
    console.log(baseBlocks);
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
                <ContextMenuNodeItem
                    blockData={blockData}
                    // key={`${Math.random()}`}
                    key={uuid()}
                />
            ))}
        </ContextMenuContent>
    );
});

export default PanelContextMenu;

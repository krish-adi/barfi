import {
    ContextMenuContent,
    ContextMenuItem,
    ContextMenuLabel,
    ContextMenuSeparator,
    ContextMenuSub,
    ContextMenuSubContent,
    ContextMenuSubTrigger,
} from "@/components/ui/context-menu";
import { useReactFlow } from "@xyflow/react";
import { useFlowUIStore } from "./flowState";

export default function PanelContextMenu() {
    const { addNodes, screenToFlowPosition } = useReactFlow();
    const contextLocation = useFlowUIStore((state) => state.contextLocation);
    const setContextLocation = useFlowUIStore(
        (state) => state.setContextLocation
    );
    return (
        <ContextMenuContent>
            <ContextMenuLabel>Add Node</ContextMenuLabel>
            <ContextMenuSeparator />
            <ContextMenuSub>
                <ContextMenuSubTrigger>Node type 1</ContextMenuSubTrigger>
                <ContextMenuSubContent>
                    <ContextMenuItem>Node 1</ContextMenuItem>
                    <ContextMenuItem>Node 2</ContextMenuItem>
                    <ContextMenuItem>Node 3</ContextMenuItem>
                </ContextMenuSubContent>
            </ContextMenuSub>
            <ContextMenuSub>
                <ContextMenuSubTrigger>Node type 2</ContextMenuSubTrigger>
                <ContextMenuSubContent>
                    <ContextMenuItem>Node 4</ContextMenuItem>
                    <ContextMenuItem>Node 5</ContextMenuItem>
                    <ContextMenuItem>Node 6</ContextMenuItem>
                </ContextMenuSubContent>
            </ContextMenuSub>
            <ContextMenuItem
                onClick={() => {
                    const flowPos = screenToFlowPosition({
                        x: contextLocation.x || 0,
                        y: contextLocation.y || 0,
                    });
                    addNodes([
                        {
                            id: `${Math.random()}`,
                            type: "default",
                            data: { label: "Simple Node" },
                            position: {
                                x: flowPos.x,
                                y: flowPos.y,
                            },
                        },
                    ]);
                    setContextLocation(undefined, undefined);
                }}
            >
                Add Simple Node
            </ContextMenuItem>
        </ContextMenuContent>
    );
}

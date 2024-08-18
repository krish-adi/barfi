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
    const { addNodes } = useReactFlow();
    const contextLocation = useFlowUIStore((state) => state.contextLocation);
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
                    console.log("event trickle", contextLocation);
                    addNodes([
                        {
                            id: `${Math.random()}`,
                            type: "default",
                            data: { label: "Simple Node" },
                            position: {
                                x: contextLocation.x,
                                y: contextLocation.y,
                            },
                        },
                    ]);
                }}
            >
                Add Simple Node
            </ContextMenuItem>
        </ContextMenuContent>
    );
}

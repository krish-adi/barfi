import {
    ContextMenuContent,
    ContextMenuItem,
    ContextMenuLabel,
    ContextMenuSeparator,
    ContextMenuSub,
    ContextMenuSubContent,
    ContextMenuSubTrigger,
} from "@/components/ui/context-menu";

export default function PanelContextMenuContent() {
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
            <ContextMenuItem>Node 7</ContextMenuItem>
        </ContextMenuContent>
    );
}

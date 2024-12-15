import { memo } from "react";
import { v4 as uuid } from "uuid";
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
import { BaseBlock } from "@/types";
import { useFlowStateStore } from "@/components/flow/flow-state";

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
                    label: `${blockData.name}-${setNodeBaseBlockCount(
                        blockData.name
                    )}`,
                };

                const flowPos = screenToFlowPosition({
                    x: contextLocation.x || 0,
                    y: contextLocation.y || 0,
                });
                const nodeId = `node__${uuid()}`;
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

const PanelContextMenu = memo(
    ({
        baseBlocks,
    }: {
        baseBlocks: BaseBlock[] | Record<string, BaseBlock[]>;
    }) => {
        return (
            <ContextMenuContent>
                <ContextMenuLabel>Add a node</ContextMenuLabel>
                <ContextMenuSeparator />
                {Array.isArray(baseBlocks)
                    ? // Handle array case
                      baseBlocks.map((blockData) => (
                          <ContextMenuNodeItem
                              blockData={blockData}
                              key={uuid()}
                          />
                      ))
                    : // Handle Record case
                      Object.entries(baseBlocks).map(([category, blocks]) => (
                          <ContextMenuSub key={category}>
                              <ContextMenuSubTrigger>
                                  {category}
                              </ContextMenuSubTrigger>
                              <ContextMenuSubContent>
                                  {blocks.map((blockData) => (
                                      <ContextMenuNodeItem
                                          blockData={blockData}
                                          key={uuid()}
                                      />
                                  ))}
                              </ContextMenuSubContent>
                          </ContextMenuSub>
                      ))}
            </ContextMenuContent>
        );
    }
);

export default PanelContextMenu;

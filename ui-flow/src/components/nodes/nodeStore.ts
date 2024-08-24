import { create } from "zustand";
import { immer } from "zustand/middleware/immer";
import { BaseBlock, BlockOptionType } from "@/types";

type NodeDataState = {
    nodes: Record<string, BaseBlock>;
    nodeOptionData: Record<string, Record<string, BlockOptionType>>;
};

type NodeDataActions = {
    addNode: (nodeId: string, nodeblock: BaseBlock) => void;
    getNodes: () => Record<string, BaseBlock>;
    mutateNodeData: (
        nodeId: string,
        optionId: string,
        value: string | number
    ) => void;
};

const useNodeDataStore = create<NodeDataState & NodeDataActions>()(
    immer((set, get) => ({
        nodes: {},
        nodeOptionData: {},
        addNode: (nodeId, nodeblock) => {
            set((state) => {
                state.nodes[nodeId] = nodeblock;
                state.nodeOptionData[nodeId] = {};
                nodeblock.options.forEach((option) => {
                    state.nodeOptionData[nodeId][option.name] = option;
                });
            });
        },
        getNodes: () => {
            return get().nodes;
        },
        mutateNodeData: (nodeId, optionId, value) => {
            set((state) => {
                if (state.nodeOptionData[nodeId]) {
                    state.nodeOptionData[nodeId][optionId].value = value;
                }
            });
        },
    }))
);

export { useNodeDataStore };

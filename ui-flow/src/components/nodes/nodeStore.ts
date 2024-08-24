import { create } from "zustand";
import { immer } from "zustand/middleware/immer";
import { BaseBlock, BlockOptionType } from "@/types";

type NodeDataState = {
    nodes: Record<string, BaseBlock>;
    nodesOptionData: Record<string, Record<string, BlockOptionType>>;
};

export type NodeDataActions = {
    addNode: (nodeId: string, nodeblock: BaseBlock) => void;
    getNodes: () => Record<string, BaseBlock>;
    getNodesOptionData: () => Record<string, Record<string, BlockOptionType>>;
    mutateNodeData: (
        nodeId: string,
        optionId: string,
        value: string | number | boolean
    ) => void;
};

const useNodeDataStore = create<NodeDataState & NodeDataActions>()(
    immer((set, get) => ({
        nodes: {},
        nodesOptionData: {},
        addNode: (nodeId, nodeblock) => {
            set((state) => {
                state.nodes[nodeId] = nodeblock;
                state.nodesOptionData[nodeId] = {};
                nodeblock.options.forEach((option) => {
                    state.nodesOptionData[nodeId][option.name] = option;
                });
            });
        },
        getNodes: () => {
            return get().nodes;
        },
        getNodesOptionData: () => {
            return get().nodesOptionData;
        },
        mutateNodeData: (nodeId, optionId, value) => {
            set((state) => {
                if (state.nodesOptionData[nodeId]) {
                    state.nodesOptionData[nodeId][optionId].value = value;
                }
            });
        },
    }))
);

export { useNodeDataStore };

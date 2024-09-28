import { create } from "zustand";
import { immer } from "zustand/middleware/immer";
import { BaseBlock, BlockOption } from "@/types";

type FlowUIState = {
    contextLocation: {
        x: number | undefined;
        y: number | undefined;
    };
    setContextLocation: (x: number | undefined, y: number | undefined) => void;
};

// This NodeDataState is to store the options' values of the nodes that have been changed by the user
// The options' values are stored in the nodesOptionData object and later retrieved by the PanelRun component
type NodeDataState = {
    nodeBaseBlockCount: Record<string, number>;
    nodes: Record<string, BaseBlock>;
    nodesOptionData: Record<string, Record<string, BlockOption>>;
};

export type NodeDataActions = {
    addNode: (nodeId: string, nodeblock: BaseBlock) => void;
    getNodes: () => Record<string, BaseBlock>;
    getNodesOptionData: () => Record<string, Record<string, BlockOption>>;
    mutateNodeData: (
        nodeId: string,
        optionId: string,
        value: string | number | boolean
    ) => void;
    setNodeBaseBlockCount: (nodeName: string) => number;
};

const useFlowStateStore = create<
    FlowUIState & NodeDataState & NodeDataActions
>()(
    immer((set, get) => ({
        contextLocation: {
            x: undefined,
            y: undefined,
        },
        setContextLocation: (x: number | undefined, y: number | undefined) =>
            set({ contextLocation: { x, y } }),
        nodes: {},
        nodeBaseBlockCount: {},
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
        setNodeBaseBlockCount: (nodeName) => {
            set((state) => {
                if (!(nodeName in state.nodeBaseBlockCount)) {
                    state.nodeBaseBlockCount[nodeName] = 1;
                } else {
                    state.nodeBaseBlockCount[nodeName]++;
                }
            });
            return get().nodeBaseBlockCount[nodeName];
        },
    }))
);

export { useFlowStateStore };

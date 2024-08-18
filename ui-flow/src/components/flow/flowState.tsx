import { create } from "zustand";

interface FlowUIState {
    contextLocation: {
        x: number | undefined;
        y: number | undefined;
    };
    setContextLocation: (x: number | undefined, y: number | undefined) => void;
    bears: number;
    increase: (by: number) => void;
}

const useFlowUIStore = create<FlowUIState>()((set) => ({
    contextLocation: {
        x: undefined,
        y: undefined,
    },
    setContextLocation: (x: number | undefined, y: number | undefined) =>
        set({ contextLocation: { x, y } }),
    bears: 0,
    increase: (by) => set((state) => ({ bears: state.bears + by })),
}));

export { useFlowUIStore };

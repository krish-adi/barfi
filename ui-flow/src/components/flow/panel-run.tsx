import { useReactFlow } from "@xyflow/react";
import { useNodeDataStore } from "@/components/nodes/nodeStore";

export default function PanelRun() {
    const { getNodes, getEdges } = useReactFlow();
    const getNodesFromStore = useNodeDataStore((state) => state.getNodes);
    return (
        <button
            className="border rounded-sm border-black px-2 py-0.5"
            onClick={() => {
                console.log(getNodes());
                console.log(getEdges());
                console.log(getNodesFromStore());
            }}
        >
            Run <span className="ml-2">🚀</span>{" "}
        </button>
    );
}

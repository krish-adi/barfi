import { useReactFlow } from "@xyflow/react";

export default function PanelRun() {
    const { getNodes } = useReactFlow();
    return (
        <button
            className="border rounded-sm border-black px-2 py-0.5"
            onClick={() => {
                console.log(getNodes());
            }}
        >
            Run <span className="ml-2">🚀</span>{" "}
        </button>
    );
}

import { useReactFlow } from "@xyflow/react";

export default function PanelRun({ onClick }: { onClick: () => void }) {
    const { getNodes } = useReactFlow();
    return (
        <button
            className="border rounded-sm border-black px-2 py-0.5"
            onClick={() => {
                console.log(getNodes());
                console.log(onClick());
            }}
        >
            Run <span className="ml-2">🚀</span>{" "}
        </button>
    );
}

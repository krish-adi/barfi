import { useCallback, memo } from "react";
import { Handle, Position } from "@xyflow/react";

const TextInputNode = memo(({ data }) => {
    const onChange = useCallback((evt: React.ChangeEvent<HTMLInputElement>) => {
        console.log(evt.target.value);
    }, []);

    return (
        <>
            <Handle type="target" position={Position.Left} id="target-1" />
            <div className="p-5 flex flex-col border rounded">
                <label htmlFor="text">Text:</label>
                <input
                    id="text"
                    name="text"
                    onChange={onChange}
                    className="border"
                />
            </div>
            <Handle type="source" position={Position.Right} id="source-1" />
            <Handle
                type="source"
                position={Position.Right}
                id="source-2"
                className="bg-pink-600"
                style={{
                    top: 30,
                }}
            />
        </>
    );
});

export default TextInputNode;

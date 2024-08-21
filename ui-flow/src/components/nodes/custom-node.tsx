import { memo } from "react";
import { Handle, Position } from "@xyflow/react";
import { BaseBlock } from "../../types";

const CustomNode = memo(
    ({
        data,
        isConnectable,
    }: {
        data: {
            blockData: BaseBlock;
        };
        isConnectable: boolean;
    }) => {
        return (
            <div className="min-w-40">
                <div
                    className="bg-zinc-700 w-full rounded-t border-zinc-700 px-2 py-0.5"
                    style={{ borderBottom: "none" }}
                >
                    <p className="text-white text-[12px]">
                        {data.blockData.name}
                    </p>
                </div>
                <div className="rounded-b border border-zinc-700 bg-white flex flex-col relative p-2">
                    {data.blockData.inputs.map((input, idx) => (
                        <p className="text-[12px] my-0.5" key={idx}>
                            {input.name}
                        </p>
                    ))}
                    {data.blockData.outputs.map((output, idx) => (
                        <p className="text-[12px] my-0.5 text-right" key={idx}>
                            {output.name}
                        </p>
                    ))}
                </div>
                {data.blockData.inputs.map((input, idx) => (
                    <Handle
                        key={idx}
                        type="target"
                        position={Position.Left}
                        id={input.name}
                        className="bg-green-600 h-2 w-2"
                        style={{
                            top: 42 + idx * 22,
                        }}
                        isConnectable={isConnectable}
                    />
                ))}
                {data.blockData.outputs.map((output, idx) => (
                    <Handle
                        key={idx}
                        type="source"
                        position={Position.Right}
                        id={output.name}
                        className="bg-pink-600 h-2 w-2"
                        style={{
                            top: "auto",
                            bottom:
                                12.75 +
                                (data.blockData.outputs.length - idx - 1) * 22,
                        }}
                        isConnectable={isConnectable}
                    />
                ))}
            </div>
        );
    }
);

export default CustomNode;

import { memo } from "react";
import { NodeProps } from "@xyflow/react";
import { Handle, Position } from "@xyflow/react";
import { BaseBlock, BlockOption } from "@/types";
import { FlowCheckbox } from "@/components/ui/checkbox";
import { FlowInput } from "@/components/ui/input";
import { FlowNumber } from "@/components/ui/input";
import { FlowSelect } from "@/components/ui/select";
import { FlowSlider } from "@/components/ui/slider";
import {
    useNodeDataStore,
    NodeDataActions,
} from "@/components/nodes/nodeStore";

// create function with a switch statement to render the correct input type
// based on the option type
const renderOption = (
    nodeId: string,
    option: BlockOption,
    mutateNodeData: NodeDataActions["mutateNodeData"],
    idx: number
) => {
    const handleChange = (newValue: string | number | boolean) => {
        mutateNodeData(nodeId, option.name, newValue);
    };
    switch (option.type) {
        case "CheckboxOption":
            return (
                <FlowCheckbox
                    key={idx}
                    id={option.name}
                    label={option.name}
                    defaultChecked={option.value}
                    onCheckedChange={handleChange}
                />
            );
        case "InputOption":
            return (
                <FlowInput
                    key={idx}
                    id={option.name}
                    placeholder={option.name}
                    defaultValue={option?.value ?? undefined}
                    onChange={(e) => handleChange(e.target.value)}
                />
            );
        case "NumberOption":
            return (
                <FlowNumber
                    key={idx}
                    id={option.name}
                    placeholder={option.name}
                    defaultValue={option?.value ?? undefined}
                    onChange={(e) => handleChange(e.target.value)}
                />
            );
        case "IntegerOption":
            return (
                <FlowNumber
                    key={idx}
                    id={option.name}
                    placeholder={option.name}
                    defaultValue={option?.value ?? undefined}
                    onChange={(e) => handleChange(e.target.value)}
                />
            );
        case "SelectOption":
            return (
                <FlowSelect
                    key={idx}
                    label={option.name}
                    options={option.items}
                    defaultValue={option?.value ?? undefined}
                    onValueChange={handleChange}
                />
            );
        case "SliderOption":
            return (
                <FlowSlider
                    key={idx}
                    id={option.name}
                    label={option.name}
                    defaultValue={option?.value ? [option?.value] : undefined}
                    max={option?.max ?? undefined}
                    min={option?.min ?? undefined}
                    step={option?.step ?? undefined}
                    onValueChange={(e) => handleChange(e[0])}
                />
            );
        default:
            return null;
    }
};

const CustomNodeBase = memo(
    ({
        id: nodeId,
        data,
        selected,
        isConnectable,
    }: {
        id: string;
        data: {
            blockData: BaseBlock;
        };
        selected: boolean;
        isConnectable: boolean;
    }) => {        
        const mutateNodeData = useNodeDataStore(
            (state) => state.mutateNodeData
        );
        return (
            <div className={`min-w-40 ${selected ? "shadow-md" : ""}`}>
                <div
                    className="bg-zinc-700 w-full rounded-t border-zinc-700 px-2 py-1"
                    style={{ borderBottom: "none" }}
                >
                    <p className="text-white text-[12px]">
                        {data.blockData.label}
                    </p>
                </div>
                <div className="rounded-b border border-zinc-700 bg-white flex flex-col relative p-2">
                    {data.blockData.inputs.map((input, idx) => (
                        <p className="text-[12px] my-0.5" key={idx}>
                            {input.name}
                        </p>
                    ))}
                    <div className="my-3 grid gap-3 w-full max-w-48">
                        {data.blockData.options.map((optionData, idx) =>
                            renderOption(
                                nodeId,
                                optionData,
                                mutateNodeData,
                                idx
                            )
                        )}
                    </div>
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

const CustomNode = (props: NodeProps) => (
    <CustomNodeBase
        {...props}
        selected={props.selected || false}
        data={{ blockData: props.data.blockData as BaseBlock }}
    />
);

export default CustomNode;

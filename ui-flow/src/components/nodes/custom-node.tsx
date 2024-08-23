import { memo } from "react";
import { Handle, Position } from "@xyflow/react";
import { BaseBlock, BlockOptionType } from "../../types";
import { FlowCheckbox } from "../ui/checkbox";
import { FlowInput } from "../ui/input";
import { FlowNumber } from "../ui/input";
import { FlowSelect } from "../ui/select";
import { FlowSlider } from "../ui/slider";

// create function with a switch statement to render the correct input type
// based on the option type
const renderOption = (option: BlockOptionType, idx: number) => {
    switch (option.type) {
        case "CheckboxOption":
            return (
                <FlowCheckbox
                    key={idx}
                    id={option.name}
                    label={option.name}
                    defaultChecked={option.value}
                />
            );
        case "InputOption":
            return (
                <FlowInput
                    key={idx}
                    id={option.name}
                    placeholder={option.name}
                    defaultValue={option?.value ?? undefined}
                />
            );
        case "NumberOption":
            return (
                <FlowNumber
                    key={idx}
                    id={option.name}
                    placeholder={option.name}
                    defaultValue={option?.value ?? undefined}
                />
            );
        case "IntegerOption":
            return (
                <FlowNumber
                    key={idx}
                    id={option.name}
                    placeholder={option.name}
                    defaultValue={option?.value ?? undefined}
                />
            );
        case "SelectOption":
            return (
                <FlowSelect
                    key={idx}
                    label={option.name}
                    options={option.items}
                    defaultValue={option?.value ?? undefined}
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
                />
            );
        default:
            return null;
    }
};

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
                    className="bg-zinc-700 w-full rounded-t border-zinc-700 px-2 py-1"
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
                    <div className="my-3 grid gap-3 w-full max-w-48">
                        {data.blockData.options.map((optionData, idx) =>
                            renderOption(optionData, idx)
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

export default CustomNode;

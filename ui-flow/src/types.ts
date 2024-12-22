import { Viewport } from "@xyflow/react";

export type BaseBlock = {
    // `name` of the base-block is the type of the Node, name and type used interchangeably
    name: string;
    type: string;
    // `label` is not used on load, but used on subsequet schema renders
    label: string | null;
    inputs: BlockInterface[];
    outputs: BlockInterface[];
    options: BlockOption[];
};

export type BlockInterface = {
    // id: string | null;
    name: string;
    value: string | number | boolean | null;
};

export type BlockOption =
    | CheckboxOption
    | InputOption
    | NumberOption
    | IntegerOption
    | SelectOption
    | SliderOption
    | DisplayOption;

export type CheckboxOption = {
    name: string;
    type: "CheckboxOption";
    value: boolean;
};

export type InputOption = {
    name: string;
    type: "InputOption";
    value: string;
};

export type NumberOption = {
    name: string;
    type: "NumberOption";
    value: number | null;
    min: number | null;
    max: number | null;
    properties: {
        min: number | null;
        max: number | null;
    };
};

export type IntegerOption = {
    name: string;
    type: "IntegerOption";
    value: number | null;
    min: number | null;
    max: number | null;
    properties: {
        min: number | null;
        max: number | null;
    };
};

export type SelectOption = {
    name: string;
    type: "SelectOption";
    value: string | null;
    items: string[];
    properties: {
        items: string[];
    };
};

export type SliderOption = {
    name: string;
    type: "SliderOption";
    value: number | null;
    min: number;
    max: number;
    step: number;
    properties: {
        min: number;
        max: number;
    };
};

export type DisplayOption = {
    name: string;
    type: "DisplayOption";
    value: string;
};

export type FlowStateNodeInterface = {
    name: string;
    value: string | number | boolean | null;
};

export type FlowStateNodeOption = {
    name: string;
    value: string | number | boolean | null;
};

export type FlowStateNode = {
    id: string; // id from the node created upon creation on flow
    type: string; // type from the blockData name from the user
    name: string;
    label: string; // label that is displayed on node in ui flow, can be changed in the future to label
    inputs: FlowStateNodeInterface[];
    outputs: FlowStateNodeInterface[];
    options: FlowStateNodeOption[];
    position: {
        x: number;
        y: number;
    };
    measured: {
        width?: number | undefined;
        height?: number | undefined;
    };
};

export type FlowStateConnection = {
    id: string;
    outputNode: string;
    outputNodeInterface: string;
    inputNode: string;
    inputNodeInterface: string;
};

export type BarfiState = {
    key: string | number | null;
    base_blocks: BaseBlock[] | Record<string, BaseBlock[]>;
    editor_schema: {
        version: string;
        nodes: FlowStateNode[];
        connections: FlowStateConnection[];
        viewport: Viewport;
    };
};

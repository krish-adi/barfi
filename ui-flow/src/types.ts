import { Viewport } from "@xyflow/react";

export type BaseBlock = {
    // `name` of the base-block is the type of the Node
    name: string;
    // `label` isn't used, need to check if this is used in the future
    label: string | null;
    inputs: BlockInterface[];
    outputs: BlockInterface[];
    options: BlockOption[];
};

export interface BlockInterface {
    id: string | null;
    name: string;
    value: string | number | boolean | null;
}

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
    display: string;
    value: string;
};

export interface FlowStateNode {
    id: string; // id from the node created upon creation on flow
    type: string; // type from the blockData name from the user
    name: string; // name that is displayed on node in ui flow, can be changed in the future to label
    inputs: [string, string | number | boolean | null][];
    outputs: [string, string | number | boolean | null][];
    options: [string, string | number | boolean | null][];
    position: {
        x: number;
        y: number;
    };
    measured: {
        width?: number | undefined;
        height?: number | undefined;
    };
}

export type FlowStateConnection = {
    id: string;
    source: string;
    target: string;
    sourceHandle: string;
    targetHandle: string;
};

export type TextOption = {
    name: string;
    type: "TextOption";
    value: string;
};

export interface BarfiStateNode {
    id: string;
    type: string;
    data: {
        blockData: BaseBlock;
    };
    position: {
        x: number;
        y: number;
    };
    measured: {
        width?: number | undefined;
        height?: number | undefined;
    };
}

export type BarfiState = {
    key: string | number | null;
    base_blocks: BaseBlock[];
    default: {
        command: string;
        editor_state: {
            nodes: BarfiStateNode[];
            connections: FlowStateConnection[];
            viewport: Viewport;
        };
    };
    editor_setting: {
        compute_engine: boolean;
    };
    load_schema_name: string;
    load_schema_names: string[];
    load_editor_schema: {
        nodes: BarfiStateNode[];
        connections: FlowStateConnection[];
        panning: {
            x: number;
            y: number;
        };
        scaling: number;
    };
};

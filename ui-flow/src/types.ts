import { Viewport } from "@xyflow/react";

export type BaseBlock = {
    name: string;
    label: string | null;
    inputs: BlockInterface[];
    outputs: BlockInterface[];
    options: BlockOption[];
};

interface BlockInterface {
    name: string;
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
    type: string; // type from the blockData type from the user
    name: string; // name that is displayed on node in ui flow, can be changed in the future
    options: [string, string | number | boolean | null][];
    interfaces: [
        string,
        {
            id: string;
            value: string | number | boolean | null;
        }
    ][];
    position: {
        x: number;
        y: number;
    };
    measured: {
        width?: number | undefined;
        height?: number | undefined;
    };
}

export type FlowStateEdge = {
    id: string;
    from: string;
    to: string;
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

export type BarfiState = {
    key: string | number | null;
    base_blocks: BaseBlock[];
    default: {
        command: string;
        editor_state: {
            nodes: FlowStateNode[];
            // edges: FlowStateEdge[];
            connections: FlowStateEdge[];
            viewport: Viewport;
        };
    };
    editor_setting: {
        compute_engine: boolean;
    };
    load_schema_name: string;
    load_schema_names: string[];
    load_editor_schema: {
        nodes: FlowStateNode[];
        connections: FlowStateEdge[];
        panning: {
            x: number;
            y: number;
        };
        scaling: number;
    };
};

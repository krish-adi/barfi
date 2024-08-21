export interface BaseBlock {
    name: string;
    inputs: { name: string }[];
    outputs: { name: string }[];
    options: string[];
}

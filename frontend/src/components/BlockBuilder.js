import { NodeBuilder } from "@baklavajs/core";

export function BlockBuilder({ BlockName, Inputs, Outputs, Options }) {
    const Block = new NodeBuilder(BlockName);
    Block.setName(BlockName);
    Inputs.forEach((input) => {
        Block.addInputInterface(
            input.name,
            input.type,
            input.value,
            input.properties
        );
    });
    Outputs.forEach((output) => {
        Block.addOutputInterface(
            output.name,
            output.type,
            output.value,
            output.properties
        );
    });
    Options.forEach((option) => {
        Block.addOption(
            option.name,
            option.type,
            option.value,
            option.sidebar,
            option.properties
        );
        // Block.addOption("ButtonOption", "ButtonOption");
    });

    return Block.build();
}

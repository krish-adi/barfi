import { NodeBuilder } from "@baklavajs/core";

export function BlockBuilder({ BlockName, Inputs, Outputs, Options }) {
    const Block = new NodeBuilder(BlockName);
    Block.setName(BlockName);
    Inputs.forEach((input) => {
        Block.addInputInterface(input.name);
    });
    Outputs.forEach((output) => {
        Block.addOutputInterface(output.name);
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

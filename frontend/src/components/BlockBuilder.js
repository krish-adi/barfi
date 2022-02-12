import { NodeBuilder } from "@baklavajs/core";

function makeid(length) {
    var result = "-id-";
    var characters = "0123456789";
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(
            Math.floor(Math.random() * charactersLength)
        );
    }
    return result;
}

export function BlockBuilder({ BlockName, Inputs, Outputs, Options }) {
    const Block = new NodeBuilder(BlockName);
    Block.setName(BlockName + makeid(6));
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

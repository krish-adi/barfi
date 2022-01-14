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
        // switch (option.type) {
        //     case "CheckboxOption":
        //         Block.addOption(
        //             option.name,
        //             "CheckboxOption",
        //             option.value,
        //             undefined
        //         );
        //         console.log(option.properties);
        //         break;
        //     case "InputOption":
        //         Block.addOption(
        //             option.name,
        //             "InputOption",
        //             option.value,
        //             undefined
        //         );
        //         break;
        //     case "IntegerOption":
        //         Block.addOption(
        //             option.name,
        //             "IntegerOption",
        //             option.value,
        //             undefined,
        //             { min: option.min, max: option.max }
        //         );
        //         break;
        //     case "NumberOption":
        //         Block.addOption(
        //             option.name,
        //             "NumberOption",
        //             option.value,
        //             undefined,
        //             { min: option.min, max: option.max }
        //         );
        //         break;
        //     case "SelectOption":
        //         Block.addOption(
        //             option.name,
        //             "SelectOption",
        //             option.value,
        //             undefined,
        //             { items: option.items }
        //         );
        //         break;
        //     case "SliderOption":
        //         Block.addOption(
        //             option.name,
        //             "SliderOption",
        //             option.value,
        //             undefined,
        //             { min: option.min, max: option.max }
        //         );
        //         break;
        //     case "TextOption":
        //         Block.addOption(
        //             option.name,
        //             "TextOption",
        //             option.value,
        //             undefined
        //         );
        //         break;
        // }
    });

    return Block.build();
}

// Block.addOption("ButtonOption", "ButtonOption");
// Block.addOption("CheckboxOption", "CheckboxOption");
// Block.addOption("InputOption", "InputOption");
// Block.addOption("IntegerOption", "IntegerOption", 5, undefined, {
//     min: 0,
//     max: 10,
// });
// Block.addOption("NumberOption", "NumberOption", 0.5, undefined, {
//     min: 0,
//     max: 1,
// });
// Block.addOption("SelectOption", "SelectOption", "Value 1", undefined, {
//     items: ["Value 1", "Value 2", "Value 3"],
// });
// Block.addOption("SliderOption", "SliderOption", 0.5);
// Block.addOption("TextOption", "TextOption", "My text");

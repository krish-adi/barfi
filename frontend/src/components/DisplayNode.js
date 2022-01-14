import { NodeBuilder } from "@baklavajs/core";

export const DisplayNode = new NodeBuilder("DisplayNode")
  .setName("Display")
  .addInputInterface("Value")
  .addOption("ValueText", "TextOption")
  .addOption("Test", "InputOption")
  .onCalculate((n) => {
    let value = n.getInterface("Value").value;
    if (typeof value === "number") {
      value = value.toFixed(3);
    }
    n.setOptionValue("ValueText", value);
  })
  .build();

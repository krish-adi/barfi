import { NodeBuilder } from "@baklavajs/core";

export function BlockBuilder({ BlockName, InputsInfo, OutputsInfo }) {
  const Block = new NodeBuilder(BlockName);
  Block.setName(BlockName);
  InputsInfo.forEach((input) => {
    Block.addInputInterface(input.name);
  });
  OutputsInfo.forEach((output) => {
    Block.addOutputInterface(output.name);
  });
  return Block.build();
}

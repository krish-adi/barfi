from typing import Union, List, Dict
from barfi.st_flow.block import Block


def prepare_blocks_export(
    base_blocks: Union[List[Block], Dict[str, List[Block]]],
):
    base_blocks_data = []
    base_blocks_list = []

    if isinstance(base_blocks, List):
        base_blocks_data = [block._export() for block in base_blocks]
        base_blocks_list = base_blocks

        return base_blocks_data, base_blocks_list

    elif isinstance(base_blocks, Dict):
        for category, block_list in base_blocks.items():
            if isinstance(block_list, List):
                for block in block_list:
                    base_blocks_list.append(block)
                    block_data = block._export()
                    block_data["category"] = category
                    base_blocks_data.append(block_data)

                return base_blocks_data, base_blocks_list
            else:
                raise TypeError(
                    "Invalid type for base_blocks passed to the st_flow component."
                )

    raise TypeError("Invalid type for base_blocks passed to the st_flow component.")

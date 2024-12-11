from typing import Union, List, Dict
from barfi.st_flow.block import Block


def prepare_blocks_export(
    base_blocks: Union[List[Block], Dict[str, List[Block]]],
):
    if isinstance(base_blocks, List):
        base_blocks_data = [block._export() for block in base_blocks]
    elif isinstance(base_blocks, Dict):
        base_blocks_data = {
            category: [block._export() for block in blocks]
            for category, blocks in base_blocks.items()
        }

    return base_blocks_data

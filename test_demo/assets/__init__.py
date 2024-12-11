from .process import process_blocks as process_blocks
from .options import options_blocks as options_blocks
from .math import math_blocks as math_blocks

base_blocks = process_blocks

base_blocks_category = {
    "Math": math_blocks,
    "Process": process_blocks,
    "Options": options_blocks,
}

from .process import process_blocks as process_blocks
from .options import options_blocks as options_blocks
from .math import math_blocks as math_blocks

base_blocks = process_blocks

base_blocks_category = {
    "process": process_blocks,
    "options": options_blocks,
    "calculator": math_blocks,
}

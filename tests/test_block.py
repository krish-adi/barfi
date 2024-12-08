from barfi.st_flow.block import Block
import pytest


def test_block_initialization():
    # Test default initialization
    block = Block()
    assert block._type.startswith("Block_")
    assert block._name.startswith("Block_")

    # Test named initialization
    named_block = Block(name="Addition")
    assert named_block._type == "Addition"
    assert named_block._name == "Addition"


def test_block_state():
    block = Block(name="StateTest")

    # Test setting and getting state
    block.set_state("counter", 0)
    assert block.get_state("counter") == 0

    # Test invalid state key
    with pytest.raises(ValueError):
        block.set_state("info", "test")  # 'info' is a reserved key

    # Test getting non-existent state
    with pytest.raises(ValueError):
        block.get_state("non_existent")


def test_block_inputs():
    block = Block(name="Addition")

    # Test default input naming
    block.add_input()
    assert "Input 1" in block._inputs
    assert block._inputs["Input 1"].value is None
    assert block._inputs["Input 1"].id is None

    # Test named input
    block.add_input(name="Number A")
    assert "Number A" in block._inputs

    # Test input with default value
    block.add_input(name="Number B", value=5)
    assert block._inputs["Number B"].value == 5

    # Test duplicate input name
    with pytest.raises(ValueError):
        block.add_input(name="Number A")


def test_block_outputs():
    block = Block(name="Addition")

    # Test default output naming
    block.add_output()
    assert "Output 1" in block._outputs
    assert block._outputs["Output 1"].value is None
    assert block._outputs["Output 1"].id is None

    # Test named output
    block.add_output(name="Sum")
    assert "Sum" in block._outputs

    # Test output with default value
    block.add_output(name="Doubled Sum", value=10)
    assert block._outputs["Doubled Sum"].value == 10

    # Test duplicate output name
    with pytest.raises(ValueError):
        block.add_output(name="Sum")

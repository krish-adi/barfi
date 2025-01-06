import pytest
from barfi.flow.block import Block
from barfi.flow.block.prepare import prepare_blocks_export


def test_prepare_blocks_export_list():
    # Arrange
    blocks = [Block(name="block1"), Block(name="block2"), Block(name="block3")]

    # Act
    result = prepare_blocks_export(blocks)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 3
    assert all(block["name"] in ["block1", "block2", "block3"] for block in result)


def test_prepare_blocks_export_dict():
    # Arrange
    blocks_dict = {
        "category1": [Block(name="block1"), Block(name="block2")],
        "category2": [Block(name="block3"), Block(name="block4")],
    }

    # Act
    result = prepare_blocks_export(blocks_dict)

    # Assert
    assert isinstance(result, dict)
    assert len(result) == 2
    assert all(block["name"] in ["block1", "block2"] for block in result["category1"])
    assert all(block["name"] in ["block3", "block4"] for block in result["category2"])


def test_prepare_blocks_export_list_duplicate_names():
    # Arrange
    blocks = [
        Block(name="block1"),
        Block(name="block2"),
        Block(name="block1"),  # Duplicate name
    ]

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        prepare_blocks_export(blocks)
    assert "Duplicate blocks found: {'block1'}" in str(exc_info.value)


def test_prepare_blocks_export_dict_duplicate_names():
    # Arrange
    blocks_dict = {
        "category1": [
            Block(name="block1"),
            Block(name="block2"),
            Block(name="block1"),  # Duplicate name
        ]
    }

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        prepare_blocks_export(blocks_dict)
    assert "Duplicate blocks found in category 'category1': {'block1'}" in str(
        exc_info.value
    )

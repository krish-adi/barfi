import pytest
from barfi.st_flow.block import Block


def test_checkbox_option():
    block = Block()

    # Test valid checkbox
    block.add_option("show_details", "checkbox", value=True)
    assert block._options["show_details"].value is True
    assert block._options["show_details"].type == "CheckboxOption"

    # Test invalid checkbox value type
    with pytest.raises(AssertionError):
        block.add_option("invalid", "checkbox", value="true")


def test_input_option():
    block = Block()

    # Test valid input
    block.add_option("name", "input", value="test")
    assert block._options["name"].value == "test"
    assert block._options["name"].type == "InputOption"

    # Test default value
    block.add_option("default", "input")
    assert block._options["default"].value == "Text input"

    # Test invalid input value type
    with pytest.raises(AssertionError):
        block.add_option("invalid", "input", value=123)


def test_integer_option():
    block = Block()

    # Test valid integer
    block.add_option("count", "integer", value=5, min=0, max=10)
    assert block._options["count"].value == 5
    assert block._options["count"].min == 0
    assert block._options["count"].max == 10

    # Test invalid integer value type
    with pytest.raises(AssertionError):
        block.add_option("invalid", "integer", value=5.5)

    # Test invalid min/max types
    with pytest.raises(AssertionError):
        block.add_option("invalid", "integer", value=5, min=0.5)


def test_number_option():
    block = Block()

    # Test valid number (integer)
    block.add_option("int_val", "number", value=5)
    assert block._options["int_val"].value == 5

    # Test valid number (float)
    block.add_option("float_val", "number", value=5.5, min=0.0, max=10.0)
    assert block._options["float_val"].value == 5.5
    assert block._options["float_val"].min == 0.0
    assert block._options["float_val"].max == 10.0

    # Test invalid number value type
    with pytest.raises(AssertionError):
        block.add_option("invalid", "number", value="5")


def test_select_option():
    block = Block()
    items = ["option1", "option2", "option3"]

    # Test valid select
    block.add_option("choice", "select", value="option1", items=items)
    assert block._options["choice"].value == "option1"
    assert block._options["choice"].items == items

    # Test empty items list
    with pytest.raises(AssertionError):
        block.add_option("invalid", "select", value="option1", items=[])

    # Test invalid value not in items
    with pytest.raises(AssertionError):
        block.add_option("invalid", "select", value="option4", items=items)

    # Test invalid items type
    with pytest.raises(AssertionError):
        block.add_option("invalid", "select", value="option1", items=[1, 2, 3])


def test_slider_option():
    block = Block()

    # Test valid slider
    block.add_option("volume", "slider", value=50, min=0, max=100)
    assert block._options["volume"].value == 50
    assert block._options["volume"].min == 0
    assert block._options["volume"].max == 100

    # Test missing min/max
    with pytest.raises(AssertionError):
        block.add_option("invalid", "slider", value=50)

    # Test value outside range
    with pytest.raises(AssertionError):
        block.add_option("invalid", "slider", value=150, min=0, max=100)


def test_display_option():
    block = Block()

    # Test valid display
    block.add_option("status", "display", value="Ready")
    assert block._options["status"].value == "Ready"
    assert block._options["status"].type == "TextOption"

    # Test default value
    block.add_option("default", "display")
    assert block._options["default"].value == "null display"

    # Test invalid display value type
    with pytest.raises(AssertionError):
        block.add_option("invalid", "display", value=123)


def test_invalid_option_type():
    block = Block()

    # Test invalid option type
    with pytest.raises(AssertionError):
        block.add_option("invalid", "unknown_type")


def test_duplicate_option_names():
    block = Block()

    # Add first option
    block.add_option("test", "input", value="first")

    # Try to add another option with the same name
    with pytest.raises(ValueError):
        block.add_option("test", "input", value="second")

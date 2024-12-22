import pytest
import json
from barfi.st_flow.flow.types import build_flow_schema_from_dict


def load_schema():
    with open("tests/assets/schema_wall.json", "r") as f:
        return json.load(f)


@pytest.fixture
def editor_schema():
    return build_flow_schema_from_dict(load_schema().get("editor_schema"))


def test_editor_schema(editor_schema):
    assert editor_schema.nodes is not None
    assert editor_schema.connections is not None
    assert editor_schema.viewport is not None


def test_nodes(editor_schema):
    # Helper function to find node by ID
    def find_node(node_id):
        return next((node for node in editor_schema.nodes if node.id == node_id), None)

    # Test each connection for validity
    for connection in editor_schema.connections:
        # Get the source and target nodes
        output_node = find_node(connection.outputNode)
        input_node = find_node(connection.inputNode)

        # Verify nodes exist
        assert output_node is not None, f"Output node {connection.outputNode} not found"
        assert input_node is not None, f"Input node {connection.inputNode} not found"

        # Verify interfaces exist
        output_interfaces = [interface.name for interface in output_node.outputs]
        input_interfaces = [interface.name for interface in input_node.inputs]

        assert (
            connection.outputNodeInterface in output_interfaces
        ), f"Output interface {connection.outputNodeInterface} not found in node {output_node.label}"
        assert (
            connection.inputNodeInterface in input_interfaces
        ), f"Input interface {connection.inputNodeInterface} not found in node {input_node.label}"


def test_connections(editor_schema):
    # Test that all connections exist
    assert len(editor_schema.connections) == 7

    # Helper function to find node by label
    def find_node_by_label(label):
        return next((node for node in editor_schema.nodes if node.label == label), None)

    # Helper function to find connection between nodes
    def find_connection(output_node_label, input_node_label):
        output_node = find_node_by_label(output_node_label)
        input_node = find_node_by_label(input_node_label)
        return next(
            (
                conn
                for conn in editor_schema.connections
                if conn.outputNode == output_node.id and conn.inputNode == input_node.id
            ),
            None,
        )

    # Test Input-1 -> Checkbox-1 connection
    connection = find_connection("Input-1", "Checkbox-1")
    assert connection is not None
    assert find_node_by_label("Input-1").name == "Input"
    assert find_node_by_label("Checkbox-1").name == "Checkbox"

    # Test Integer-1 -> Select-1 connection
    connection = find_connection("Integer-1", "Select-1")
    assert connection is not None
    assert find_node_by_label("Integer-1").name == "Integer"
    assert find_node_by_label("Select-1").name == "Select"

    # Test Integer-2 -> Slider-1 connection
    connection = find_connection("Number-1", "Slider-1")
    assert connection is not None
    assert find_node_by_label("Number-1").name == "Number"
    assert find_node_by_label("Slider-1").name == "Slider"

    # Test Checkbox-1 -> Mixer-1 connection
    connection = find_connection("Checkbox-1", "Three Mixer-1")
    assert connection is not None

    # Test Select-1 -> Mixer-1 connection
    connection = find_connection("Select-1", "Three Mixer-1")
    assert connection is not None

    # Test Slider-1 -> Mixer-2 connection
    connection = find_connection("Slider-1", "Three Mixer-1")
    assert connection is not None

    # Test Mixer-2 -> Result-1 connection
    connection = find_connection("Three Mixer-1", "Result-1")
    assert connection is not None


def test_options(editor_schema):
    # Helper function to find node by label
    def find_node_by_label(label):
        return next((node for node in editor_schema.nodes if node.label == label), None)

    # Test Input-1 options
    input_node = find_node_by_label("Input-1")
    assert input_node.name == "Input"
    assert len(input_node.options) == 2
    assert any(
        opt.name == "display-option"
        and opt.value == "This is a Block with Input option."
        for opt in input_node.options
    )
    assert any(
        opt.name == "input-option" and opt.value == "hello there"
        for opt in input_node.options
    )

    # Test Checkbox-1 options
    checkbox_node = find_node_by_label("Checkbox-1")
    assert checkbox_node.name == "Checkbox"
    assert len(checkbox_node.options) == 2
    assert any(
        opt.name == "display-option"
        and opt.value == "This is a Block with Checkbox option."
        for opt in checkbox_node.options
    )
    assert any(
        opt.name == "checkbox-option" and opt.value is True
        for opt in checkbox_node.options
    )

    # Test Integer-1 options
    integer_node = find_node_by_label("Integer-1")
    assert integer_node.name == "Integer"
    assert len(integer_node.options) == 2
    assert any(
        opt.name == "display-option"
        and opt.value == "This is a Block with Integer option."
        for opt in integer_node.options
    )
    assert any(
        opt.name == "integer-option" and opt.value == 3 for opt in integer_node.options
    )

    # Test Integer-2 options
    number_node = find_node_by_label("Number-1")
    assert number_node.name == "Number"
    assert len(number_node.options) == 2
    assert any(
        opt.name == "display-option"
        and opt.value == "This is a Block with Number option."
        for opt in number_node.options
    )
    assert any(
        opt.name == "number-option" and opt.value == 7 for opt in number_node.options
    )

    # Test Select-1 options
    select_node = find_node_by_label("Select-1")
    assert select_node.name == "Select"
    assert len(select_node.options) == 2
    assert any(
        opt.name == "display-option"
        and opt.value == "This is a Block with Select option."
        for opt in select_node.options
    )
    assert any(
        opt.name == "select-option" and opt.value == "Select B"
        for opt in select_node.options
    )

    # Test Slider-1 options
    slider_node = find_node_by_label("Slider-1")
    assert slider_node.name == "Slider"
    assert len(slider_node.options) == 2
    assert any(
        opt.name == "display-option"
        and opt.value == "This is a Block with Slider option."
        for opt in slider_node.options
    )
    assert any(
        opt.name == "slider-option" and opt.value == 4 for opt in slider_node.options
    )

    # Test Mixer nodes have no options
    mixer_1 = find_node_by_label("Three Mixer-1")
    assert mixer_1.name == "Three Mixer"
    assert len(mixer_1.options) == 0

    # Test Result node has no options
    result = find_node_by_label("Result-1")
    assert result.name == "Result"
    assert len(result.options) == 0


def test_options_values(editor_schema):
    # Helper function to find node by label
    def find_node_by_label(label):
        return next((node for node in editor_schema.nodes if node.label == label), None)

    # Test Input-1 value
    input_node = find_node_by_label("Input-1")
    input_option = next(
        (opt for opt in input_node.options if opt.name == "input-option"), None
    )
    assert input_option is not None
    assert input_option.value == "hello there"

    # Test Integer-1 value
    integer_1 = find_node_by_label("Integer-1")
    integer_1_option = next(
        (opt for opt in integer_1.options if opt.name == "integer-option"), None
    )
    assert integer_1_option is not None
    assert integer_1_option.value == 3

    # Test Integer-2 value
    number_1 = find_node_by_label("Number-1")
    number_1_option = next(
        (opt for opt in number_1.options if opt.name == "number-option"), None
    )
    assert number_1_option is not None
    assert number_1_option.value == 7

    # Test Checkbox-1 value
    checkbox = find_node_by_label("Checkbox-1")
    checkbox_option = next(
        (opt for opt in checkbox.options if opt.name == "checkbox-option"), None
    )
    assert checkbox_option is not None
    assert checkbox_option.value is True

    # Test Select-1 value
    select = find_node_by_label("Select-1")
    select_option = next(
        (opt for opt in select.options if opt.name == "select-option"), None
    )
    assert select_option is not None
    assert select_option.value == "Select B"

    # Test Slider-1 value
    slider = find_node_by_label("Slider-1")
    slider_option = next(
        (opt for opt in slider.options if opt.name == "slider-option"), None
    )
    assert slider_option is not None
    assert slider_option.value == 4

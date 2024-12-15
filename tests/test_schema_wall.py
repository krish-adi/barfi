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
        output_interfaces = [interface[0] for interface in output_node.outputs]
        input_interfaces = [interface[0] for interface in input_node.inputs]

        assert (
            connection.outputNodeInterface in output_interfaces
        ), f"Output interface {connection.outputNodeInterface} not found in node {output_node.name}"
        assert (
            connection.inputNodeInterface in input_interfaces
        ), f"Input interface {connection.inputNodeInterface} not found in node {input_node.name}"


def test_connections(editor_schema):
    # Test that all connections exist
    assert len(editor_schema.connections) == 8

    # Helper function to find node by name
    def find_node_by_name(name):
        return next((node for node in editor_schema.nodes if node.name == name), None)

    # Helper function to find connection between nodes
    def find_connection(output_node_name, input_node_name):
        output_node = find_node_by_name(output_node_name)
        input_node = find_node_by_name(input_node_name)
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
    assert find_node_by_name("Input-1").type == "Input"
    assert find_node_by_name("Checkbox-1").type == "Checkbox"

    # Test Integer-1 -> Select-1 connection
    connection = find_connection("Integer-1", "Select-1")
    assert connection is not None
    assert find_node_by_name("Integer-1").type == "Integer"
    assert find_node_by_name("Select-1").type == "Select"

    # Test Integer-2 -> Slider-1 connection
    connection = find_connection("Integer-2", "Slider-1")
    assert connection is not None
    assert find_node_by_name("Integer-2").type == "Integer"
    assert find_node_by_name("Slider-1").type == "Slider"

    # Test Checkbox-1 -> Mixer-1 connection
    connection = find_connection("Checkbox-1", "Mixer-1")
    assert connection is not None

    # Test Select-1 -> Mixer-1 connection
    connection = find_connection("Select-1", "Mixer-1")
    assert connection is not None

    # Test Mixer-1 -> Mixer-2 connection
    connection = find_connection("Mixer-1", "Mixer-2")
    assert connection is not None

    # Test Slider-1 -> Mixer-2 connection
    connection = find_connection("Slider-1", "Mixer-2")
    assert connection is not None

    # Test Mixer-2 -> Result-1 connection
    connection = find_connection("Mixer-2", "Result-1")
    assert connection is not None


def test_options(editor_schema):
    # Helper function to find node by name
    def find_node_by_name(name):
        return next((node for node in editor_schema.nodes if node.name == name), None)

    # Test Input-1 options
    input_node = find_node_by_name("Input-1")
    assert input_node.type == "Input"
    assert len(input_node.options) == 2
    assert [
        "display-option",
        "TextOption",
        "This is a Block with Input option.",
    ] in input_node.options
    assert ["input-option", "InputOption", "hello there"] in input_node.options

    # Test Checkbox-1 options
    checkbox_node = find_node_by_name("Checkbox-1")
    assert checkbox_node.type == "Checkbox"
    assert len(checkbox_node.options) == 2
    assert [
        "display-option",
        "TextOption",
        "This is a Block with Checkbox option.",
    ] in checkbox_node.options
    assert ["checkbox-option", "CheckboxOption", True] in checkbox_node.options

    # Test Integer-1 options
    integer_node = find_node_by_name("Integer-1")
    assert integer_node.type == "Integer"
    assert len(integer_node.options) == 2
    assert [
        "display-option",
        "TextOption",
        "This is a Block with Integer option.",
    ] in integer_node.options
    assert ["integer-option", "IntegerOption", "7"] in integer_node.options

    # Test Integer-2 options
    integer_node_2 = find_node_by_name("Integer-2")
    assert integer_node_2.type == "Integer"
    assert len(integer_node_2.options) == 2
    assert [
        "display-option",
        "TextOption",
        "This is a Block with Integer option.",
    ] in integer_node_2.options
    assert ["integer-option", "IntegerOption", "3"] in integer_node_2.options

    # Test Select-1 options
    select_node = find_node_by_name("Select-1")
    assert select_node.type == "Select"
    assert len(select_node.options) == 2
    assert [
        "display-option",
        "TextOption",
        "This is a Block with Select option.",
    ] in select_node.options
    assert ["select-option", "SelectOption", "Select B"] in select_node.options

    # Test Slider-1 options
    slider_node = find_node_by_name("Slider-1")
    assert slider_node.type == "Slider"
    assert len(slider_node.options) == 2
    assert [
        "display-option",
        "TextOption",
        "This is a Block with Slider option.",
    ] in slider_node.options
    assert ["slider-option", "SliderOption", 4] in slider_node.options

    # Test Mixer nodes have no options
    mixer_1 = find_node_by_name("Mixer-1")
    assert mixer_1.type == "Mixer"
    assert len(mixer_1.options) == 0

    mixer_2 = find_node_by_name("Mixer-2")
    assert mixer_2.type == "Mixer"
    assert len(mixer_2.options) == 0

    # Test Result node has no options
    result = find_node_by_name("Result-1")
    assert result.type == "Result"
    assert len(result.options) == 0


def test_options_values(editor_schema):
    # Helper function to find node by name
    def find_node_by_name(name):
        return next((node for node in editor_schema.nodes if node.name == name), None)

    # Test Input-1 value
    input_node = find_node_by_name("Input-1")
    input_option = next(
        (opt for opt in input_node.options if opt[0] == "input-option"), None
    )
    assert input_option is not None
    assert input_option[2] == "hello there"

    # Test Integer-1 value
    integer_1 = find_node_by_name("Integer-1")
    integer_1_option = next(
        (opt for opt in integer_1.options if opt[0] == "integer-option"), None
    )
    assert integer_1_option is not None
    assert integer_1_option[2] == "7"

    # Test Integer-2 value
    integer_2 = find_node_by_name("Integer-2")
    integer_2_option = next(
        (opt for opt in integer_2.options if opt[0] == "integer-option"), None
    )
    assert integer_2_option is not None
    assert integer_2_option[2] == "3"

    # Test Checkbox-1 value
    checkbox = find_node_by_name("Checkbox-1")
    checkbox_option = next(
        (opt for opt in checkbox.options if opt[0] == "checkbox-option"), None
    )
    assert checkbox_option is not None
    assert checkbox_option[2] is True

    # Test Select-1 value
    select = find_node_by_name("Select-1")
    select_option = next(
        (opt for opt in select.options if opt[0] == "select-option"), None
    )
    assert select_option is not None
    assert select_option[2] == "Select B"

    # Test Slider-1 value
    slider = find_node_by_name("Slider-1")
    slider_option = next(
        (opt for opt in slider.options if opt[0] == "slider-option"), None
    )
    assert slider_option is not None
    assert slider_option[2] == 4

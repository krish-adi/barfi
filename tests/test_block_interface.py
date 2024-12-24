import pytest
from typing import Dict, List, Any, Union
from dataclasses import dataclass
from barfi.flow.block.interface import (
    IT,
    BlockInterface,
    check_block_interface_type_equality,
    is_valid_interface_type,
)


# Generic function that takes type as parameter
def create_typed_interface(name: str, itype: IT) -> BlockInterface[IT]:
    is_valid_interface_type(itype)
    return BlockInterface[itype](name=name)


def test_simple_type_creation():
    """Test creation of BlockInterface with simple types"""
    simple_types = [int, str, float, bool, dict, list, tuple, set]

    for type_ in simple_types:
        interface = create_typed_interface(name="test", itype=type_)
        assert interface.name == "test"
        assert interface.value is None


def test_complex_type_creation():
    """Test creation of BlockInterface with complex types"""
    complex_types = [
        Any,
        List,
        List[str],
        List[int],
        Dict,
        Dict[str, int],
        Union[str, int],
    ]

    for type_ in complex_types:
        interface = create_typed_interface(name="test", itype=type_)
        assert interface.name == "test"
        assert interface.value is None


def test_custom_type_creation():
    @dataclass
    class TestDataClass:
        name: str
        age: int

    class TestClass:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age

    """Test creation of BlockInterface with custom classes and dataclasses"""
    custom_types = [TestClass, TestDataClass, Dict[str, TestClass], List[TestDataClass]]

    for type_ in custom_types:
        interface = create_typed_interface(name="test", itype=type_)
        assert interface.name == "test"
        assert interface.value is None


def test_interface_export():
    """Test export functionality of BlockInterface"""
    # Test simple type export
    int_interface = create_typed_interface(name="int_test", itype=int)
    export_data = int_interface.export()
    assert export_data["name"] == "int_test"
    assert "type.<class 'int'>" == export_data["itype"]

    # Test Any type export
    any_interface = create_typed_interface(name="any_test", itype=Any)
    export_data = any_interface.export()
    assert export_data["name"] == "any_test"
    assert "typing.Any" == export_data["itype"]

    # Test complex type export
    list_str_interface = create_typed_interface(name="list_str_test", itype=List[str])
    export_data = list_str_interface.export()
    assert export_data["name"] == "list_str_test"
    assert "typing.List[str]" == export_data["itype"]


def test_interface_type_equality():
    """Test type equality checking between BlockInterfaces"""
    # Same types should be equal
    assert check_block_interface_type_equality(
        create_typed_interface(name="test1", itype=int),
        create_typed_interface(name="test2", itype=int),
    )

    # Different types should not be equal
    assert not check_block_interface_type_equality(
        create_typed_interface(name="test1", itype=int),
        create_typed_interface(name="test2", itype=str),
    )

    # Complex types with same structure should be equal
    assert check_block_interface_type_equality(
        create_typed_interface(name="test1", itype=Union[str, int]),
        create_typed_interface(name="test2", itype=Union[str, int]),
    )


def test_invalid_interface_types():
    """Test validation of interface types"""
    # Invalid type should raise TypeError
    with pytest.raises(TypeError):
        is_valid_interface_type("not_a_type")

    # String literal should raise TypeError
    with pytest.raises(TypeError):
        create_typed_interface(name="test1", itype="string")


def test_interface_value_assignment():
    """Test value assignment to BlockInterface"""
    # Test valid value assignment
    interface = create_typed_interface(name="test", itype=int)
    interface.set_value(42)
    assert interface.value == 42

    # Test invalid value assignment
    with pytest.raises(ValueError):
        interface.set_value("not an int")

    # Test with complex type - valid assignment
    list_interface = create_typed_interface(name="test", itype=List[str])
    list_interface.set_value(["a", "b", "c"])
    assert list_interface.value == ["a", "b", "c"]

    # Test with complex type - invalid assignment
    with pytest.raises(ValueError):
        list_interface.set_value(
            [1, 2, 3]
        )  # Should fail as these are ints, not strings

    @dataclass
    class TestDataClass:
        name: str
        age: int

    class TestClass:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age

    # Test with dataclass - valid assignment
    dataclass_interface = create_typed_interface(name="test", itype=TestDataClass)
    dataclass_interface.set_value(TestDataClass(name="John", age=30))

    # Test with dataclass - invalid assignment
    with pytest.raises(ValueError):
        dataclass_interface.set_value(
            {"name": "John", "age": 30}
        )  # Should fail as these are ints, not strings

    # Test with class - valid assignment
    class_interface = create_typed_interface(name="test", itype=TestClass)
    class_interface.set_value(TestClass(name="John", age=30))

    # Test with class - invalid assignment
    with pytest.raises(ValueError):
        class_interface.set_value(
            {"name": "Jane", "age": 25}
        )  # Should fail as these are ints, not strings

    list_dataclass_interface = create_typed_interface(
        name="test", itype=List[TestDataClass]
    )
    list_dataclass_interface.set_value(
        [TestDataClass(name="John", age=30), TestDataClass(name="Jane", age=25)]
    )

    # Test with list of classes - invalid assignment
    with pytest.raises(ValueError):
        list_dataclass_interface.set_value(
            [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        )

    # Test with dict of classes - valid assignment
    dict_class_interface = create_typed_interface(
        name="test", itype=Dict[str, TestClass]
    )
    dict_class_interface.set_value(
        {"john": TestClass(name="John", age=30), "jane": TestClass(name="Jane", age=25)}
    )

    # Test with dict of dataclasses - invalid assignment
    with pytest.raises(ValueError):
        dict_class_interface.set_value(
            {"john": {"name": "John", "age": 30}, "jane": {"name": "Jane", "age": 25}}
        )

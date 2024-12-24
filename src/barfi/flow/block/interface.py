import warnings
from typing import TypeVar, Generic, Type, get_origin, Any, get_args
from dataclasses import dataclass, is_dataclass

# generic type for the interface value
IT = TypeVar("IT")


@dataclass
class BlockInterface(Generic[IT]):
    name: str
    value: IT = None

    def export(self) -> dict:
        interface_type = get_args(self.__orig_class__)[0]
        type_string = ""

        if interface_type is Any:
            type_string = "typing.Any"

        # Check if it's a dataclass
        if is_dataclass(interface_type) and type_string == "":
            type_string = "dataclass." + str(interface_type)

        # Check if it's a built-in type
        if isinstance(interface_type, type) and type_string == "":
            type_string = "type." + str(interface_type)

        # Check for other complex typing types from the typing module
        if get_origin(interface_type) is not None and type_string == "":
            type_string = str(interface_type)

        return {
            "name": self.name,
            "itype": type_string,
        }

    def set_value(self, value: IT):
        interface_type = get_args(self.__orig_class__)[0]
        # Handle generic types from typing module
        if interface_type is Any:
            pass
        elif get_origin(interface_type) is not None:
            # For generic types like List[str], Dict[str, int] etc.
            origin_type = get_origin(interface_type)
            print("origin_type", origin_type)
            type_args = get_args(interface_type)
            print("type_args", type_args)

            if not isinstance(value, origin_type):
                raise ValueError(
                    f"Value {value} is not of type {interface_type}. Interface type is {interface_type}."
                )

            # Check inner types for containers
            if isinstance(value, (list, set, tuple)):
                if not all(isinstance(x, type_args[0]) for x in value):
                    raise ValueError(
                        f"Not all elements in {value} match the required type {type_args[0]}"
                    )
            elif isinstance(value, dict):
                if not all(
                    isinstance(k, type_args[0]) and isinstance(v, type_args[1])
                    for k, v in value.items()
                ):
                    raise ValueError(
                        f"Not all key-value pairs in {value} match the required types {type_args[0]}, {type_args[1]}"
                    )
        else:
            # For non-generic types (int, str, etc.)
            if not isinstance(value, interface_type):
                raise ValueError(
                    f"Value {value} is not of type {interface_type}. Interface type is {interface_type}."
                )

        self.value = value


def check_block_interface_type_equality(
    interface_1: BlockInterface, interface_2: BlockInterface
) -> bool:
    interface_1_type = get_args(interface_1.__orig_class__)[0]
    interface_2_type = get_args(interface_2.__orig_class__)[0]
    return interface_1_type == interface_2_type


def is_valid_interface_type(interface_type: Type):
    """
    Validates if the provided type is acceptable as a block interface type.

    Args:
        interface_type (Type): The type to validate.

    Returns:
        None

    Raises:
        TypeError: If the interface_type is not one of:
            - A Python built-in type (str, int, etc.)
            - A typing module type (List, Dict, etc.)
            - A dataclass

    Examples:
        >>> is_valid_interface_type(str)  # Valid
        >>> is_valid_interface_type(List[int])  # Valid
        >>> is_valid_interface_type(MyDataClass)  # Valid if MyDataClass is a dataclass
    """
    _valid = False

    # Check if it's Any type and warn about its usage
    if interface_type is Any:
        # TODO: add a logger and add this to it as a warning.
        warnings.warn(
            "Using 'Any' type is discouraged as it bypasses type checking. "
            "This should only be used for local testing and not in production code.",
            UserWarning,
            stacklevel=0,
        )
        _valid = True

    # Check if it's a built-in type
    if isinstance(interface_type, type):
        # print("type", interface_type)
        _valid = True

    # Check if it's a dataclass
    if is_dataclass(interface_type):
        # print("dataclass", interface_type)
        _valid = True

    # Check for other complex typing types from the typing module
    if get_origin(interface_type) is not None:
        # print("typing", interface_type)
        _valid = True

    if not _valid:
        raise TypeError(
            f"{interface_type} is not a valid type. Must be a Python base type, a typing module type, or a dataclass."
        )

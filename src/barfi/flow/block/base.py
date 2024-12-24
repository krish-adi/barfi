import types
import uuid
from typing import Callable, Any, Dict, List, Type
from dataclasses import asdict, dataclass, field
from barfi.flow.block.option import BlockOption, BlockOptionValue
from barfi.flow.block.interface import BlockInterface, IT, is_valid_interface_type


@dataclass
class Block:
    # Public fields
    name: str = "Block"

    # Private fields (excluded from init and compare)
    _type: str = field(init=False, repr=False, compare=False)
    _inputs: Dict[str, BlockInterface] = field(
        init=False, default_factory=dict, compare=False
    )
    _outputs: Dict[str, BlockInterface] = field(
        init=False, default_factory=dict, compare=False
    )
    _options: Dict[str, BlockOption] = field(
        init=False, default_factory=dict, compare=False
    )
    _state: Dict[str, object] = field(
        init=False, default_factory=lambda: {"info": None}, repr=False, compare=False
    )
    _interface_names: List[str] = field(
        init=False, default_factory=list, repr=False, compare=False
    )

    def __post_init__(self):
        """
        Post-initialization to set up private fields based on the given `name`.
        """
        # Generate a unique name if the default is used
        if self.name == "Block":
            self.name = f"Block_{str(uuid.uuid4()).replace('-', '_')}"

        # Set the type to match the name
        self._type = self.name

    def add_input(self, name: str = None, interface_type: Type[IT] = Any) -> None:
        """
        Add an Input interface to the Block

        Args:
            name (str, optional): The name of the Input interface. If None, a default name will be generated.
            interface_type (Type[IT], optional): The type of the interface. Defaults to Any.
                Must be a Python built-in type, typing module type, or dataclass.

        Raises:
            ValueError: If the name already exists as an interface to the Block.
            TypeError: If the interface_type is not a valid type.

        Examples:
            >>> block.add_input(name='Input Name', interface_type=int)
        """
        is_valid_interface_type(interface_type)

        if name is None:
            name = f"Input {len(self._inputs) + 1}"

        if name in self._interface_names:
            raise ValueError(
                f"name: {name} already exists as an interface to the Block."
            )

        self._inputs[name] = BlockInterface[interface_type](name=name)
        self._interface_names.append(name)

    def add_output(self, name: str = None, interface_type: Type[IT] = Any) -> None:
        """
        Add an Output interface to the Block

        Args:
            name (str, optional): The name of the Output interface. If None, a default name will be generated.
            interface_type (Type[IT], optional): The type of the interface. Defaults to Any.
                Must be a Python built-in type, typing module type, or dataclass.

        Raises:
            ValueError: If the name already exists as an interface to the Block.
            TypeError: If the interface_type is not a valid type.

        Examples:
            >>> block.add_output(name='Output Name', interface_type=str)
        """
        is_valid_interface_type(interface_type)

        if name is None:
            name = f"Output {len(self._outputs) + 1}"

        if name in self._interface_names:
            raise ValueError(
                f"name: {name} already exists as an interface to the Block."
            )

        self._outputs[name] = BlockInterface[interface_type](name=name)
        self._interface_names.append(name)

    def get_interface(self, name: str):
        """
        Get the value of a given interface.

        Args:
            name (str): The name of the interface.

        Returns:
            The value of the interface.

        Raises:
            ValueError: If no interface with the given name is found.
        """
        if name in self._inputs:
            return self._inputs[name].value
        elif name in self._outputs:
            return self._outputs[name].value
        else:
            raise ValueError(f"No interface with name: {name} found for Block")

    def set_interface(self, name: str, value) -> None:
        """
        Set the value for a given interface.

        Args:
            name (str): The name of the interface.
            value: The value to set for the interface.

        Raises:
            ValueError: If no interface with the given name is found.
        """
        if name in self._inputs:
            self._inputs[name].set_value(value)
        elif name in self._outputs:
            self._outputs[name].set_value(value)
        else:
            raise ValueError(f"No interface with name: {name} found for Block")

    def set_state(self, key: str, value: Any) -> None:
        """
        Set a state value for the block.
        Reserved keys: ['info']

        Args:
            key (str): The key for the state value.
            value (Any): The value to set for the state.

        Raises:
            ValueError: If the key is a reserved state key.
        """
        reserved_state_keys = ["info"]
        if key in reserved_state_keys:
            raise ValueError(
                f"Key: {key} used for setting state of block is reserved. Use another key."
            )
        else:
            self._state[key] = value

    def get_state(self, key: str) -> Any:
        """
        Get a state value for the block.

        Args:
            key (str): The key for the state value.

        Returns:
            The value of the state.
        """
        if key in self._state:
            return self._state[key]
        else:
            raise ValueError(f"Key: {key} does not exist in state.")

    def add_option(self, name: str, type: str, **kwargs) -> None:
        """
        Add an interactive Option interface to the Block.

        Args:
            name (str): The name of the Option interface.
            type (str): The type of the Option interface. Must be one of: 'checkbox', 'input', 'integer', 'number', 'select', 'slider', 'display'.
            **kwargs: Additional properties depending on the type of Option interface.

        Raises:
            ValueError: If an option with the given name already exists in the Block.
            AssertionError: If the name or type arguments are not strings, or if the type is not a valid option type.

        Examples:
            >>> block.add_option(name='My Option', type='checkbox', value=True)
        """

        assert isinstance(name, str), "Error: 'name' argument should be of type string."
        assert isinstance(type, str), "Error: 'type' argument should be of type string."
        assert type in [
            "checkbox",
            "input",
            "integer",
            "number",
            "select",
            "slider",
            "display",
        ], 'Error: Option "type" is not a standard Option interface parameter.'

        if name in self._options:
            raise ValueError(f"Option with name: {name} already exists in Block.")

        option = BlockOption.build(name, type, kwargs)
        self._options[name] = option

    def set_option(self, name: str, **kwargs) -> None:
        """
        Set the value of an existing Option interface in the Block.

        Args:
            name (str): The name of the Option interface.
            **kwargs: Additional properties to set for the Option. Currently, only 'value' can be set.

        Raises:
            ValueError: If the option name doesn't exist, if trying to set an invalid property,
                        or if the property is not valid for the given option.

        Examples:
            >>> block.set_option('My Option', value=False)
        """
        if name in self._options:
            for arg, value in kwargs.items():
                if arg in self._options[name].__dict__:
                    if arg == "value":
                        setattr(self._options[name], arg, value)
                    else:
                        raise ValueError(
                            f"Cannot set or invalid property: {arg} for Block option."
                        )
                else:
                    raise ValueError(
                        f"Property: {arg} is not a valid option property for {name}."
                    )
        else:
            raise ValueError(f"Option name: {name} does not exist in Block.")

    def get_option(self, name: str) -> BlockOptionValue:
        """
        Get the value of an existing Option interface in the Block.

        Args:
            name (str): The name of the Option interface.

        Returns:
            Value: The value of the Option interface.

        Raises:
            ValueError: If the option name doesn't exist in the Block.

        Examples:
            >>> value = block.get_option('My Option')
        """
        if name in self._options:
            return self._options[name].value
        else:
            raise ValueError(f"Option name: {name} does not exist in Block.")

    def _export(self) -> dict:
        """
        Export the block's data as a dictionary.

        Returns:
            dict: A dictionary containing the block's name, inputs, outputs, and options.
                  The inputs, outputs, and options are exported as lists of their respective values.

        This method is used internally to serialize the block's data for saving or transmitting.
        """
        return {
            "name": self.name,
            "type": self._type,
            "inputs": [input.export() for input in self._inputs.values()],
            "outputs": [output.export() for output in self._outputs.values()],
            "options": [asdict(option) for option in self._options.values()],
        }

    def _on_compute(self) -> None:
        """
        Default compute method for the block.
        This method is meant to be overridden by the user-defined compute function.
        """
        pass

    def add_compute(self, _func: Callable[["Block"], None]) -> None:
        """
        Add a compute function to the block.

        Args:
            _func (Callable[['Block'], None]): The compute function to be added.
                It should take a single argument of type 'Block' (self) and return None.

        This method binds the provided function to the block instance,
        allowing it to access and modify the block's attributes.
        """
        self._on_compute = types.MethodType(_func, self)

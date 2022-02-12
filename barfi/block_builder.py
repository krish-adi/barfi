import types
from typing import Callable
from .option_builder import build_option


class Block(object):
    _interfaceVariables = ['name']

    def __init__(self, name: str = 'Block') -> None:
        # Initialise the Block object

        # To set the name of the Block, default = Block
        # Reference to the type of the Block
        self._type = name
        # Title of the block on the editor
        self._name = name

        # To set the defaults for inputs, outputs, options
        self._inputs = []
        self._outputs = []
        self._options = []

        self._interface_value = {}

    def __repr__(self) -> str:
        return f"<barfi.Block of type '{self._type}' at {hex(id(self))}>"

    def __str__(self) -> str:
        line_1 = f"barfi.Block of type '{self._type}' with name '{self._name}'\n"
        inputs_name = [input['name'] for input in self._inputs]
        outputs_name = [output['name'] for output in self._outputs]
        options_name = [option['name'] for option in self._options]
        line_2 = f"Inputs: {inputs_name!r}\n"
        line_3 = f"Outputs: {outputs_name!r}\n"
        line_4 = f"Options: {options_name!r}"
        return line_1 + line_2 + line_3 + line_4

    def add_input(self, **kwargs) -> None:
        """
        A function defined to add an Input interface to the Block

        Use as:
            self.addInput(**kwargs)

        Interface options:
            name (str)  : The name of the Input interface.
        """

        input = {}
        if not bool(kwargs):
            in_nos = len(self._inputs)
            input['name'] = 'Input ' + str(in_nos + 1)
        else:
            for arg in kwargs:
                if arg not in list(self._interfaceVariables):
                    raise(
                        'Error: Argument passed not in the list of Input interface parameters.')
                arg_val = kwargs.get(arg)
                input[arg] = arg_val

        self._inputs.append(input)

    def add_output(self, **kwargs) -> None:
        """
        A function defined to add an Output interface to the Block

        Use as:
            self.addOutput(**kwargs)

        Interface options:
            name (str)  : The name of the Output interface.
        """

        output = {}
        if not bool(kwargs):
            in_nos = len(self._outputs)
            output['name'] = 'Output ' + str(in_nos + 1)
        else:
            for arg in kwargs:
                if arg not in list(self._interfaceVariables):
                    raise(
                        'Error: Argument passed not in the list of Input interface parameters.')
                arg_val = kwargs.get(arg)
                output[arg] = arg_val

        self._outputs.append(output)

    def add_option(self, name: str, type: str, **kwargs) -> None:
        """
        A function defined to add interactive Option interface to the Block

        Use as:
            self.addOption(name=name, type=type, **kwargs)

        Interactive options interface:
            name (str)  : The name of the Option interface.
            type (str)  : The type of the Option interface. 'checkbox', 'input', 'integer', 'number', 'select', 'slider', 'text'.
            value       : The default value for the option. Depends on the option chosen.

            Additional properties depending on the type of Option interface.

        """

        assert isinstance(
            name, str), "Error: 'name' argument should be of type string."
        assert isinstance(
            type, str), "Error: 'type' argument should be of type string."
        assert type in ['checkbox', 'input', 'integer', 'number', 'select', 'slider',
                        'display'], 'Error: Option "type" is not of standard Option interface parameter.'

        _option = build_option(name, type, kwargs)

        self._options.append(_option)

    def _export(self):
        return {'name': self._name, 'inputs': self._inputs, 'outputs': self._outputs, 'options': self._options}

    def get_interface(self, name):
        return self._interface_value[name]['value']

    def set_interface(self, name, value) -> None:
        self._interface_value[name]['value'] = value

    def _on_calculate():
        pass

    def add_calculate(self, _func: Callable):
        self._on_calculate = types.MethodType(_func, self)

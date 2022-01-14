import types
from typing import Callable


class Block(object):
    """

    """

    _interfaceVariables = ['name']

    def __init__(self, **kwargs) -> None:
        # Initialise the Block object

        # To set the name of the Block, default = Block
        self.name = kwargs.get('name', 'Block')
        # self.title = kwargs.get('title', 'Block') # Title of the block on the editor

        # To set the defaults for inputs, outputs, options
        self.inputs = []
        self.outputs = []
        self.options = []

    def __repr__(self) -> str:
        return super().__repr__()

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
            in_nos = len(self.inputs)
            input['name'] = 'Input ' + str(in_nos + 1)
        else:
            for arg in kwargs:
                if arg not in list(self._interfaceVariables):
                    raise(
                        'Error: Argument passed not in the list of Input interface parameters.')
                arg_val = kwargs.get(arg)
                input[arg] = arg_val

        self.inputs.append(input)

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
            in_nos = len(self.outputs)
            output['name'] = 'Output ' + str(in_nos + 1)
        else:
            for arg in kwargs:
                if arg not in list(self._interfaceVariables):
                    raise(
                        'Error: Argument passed not in the list of Input interface parameters.')
                arg_val = kwargs.get(arg)
                output[arg] = arg_val

        self.outputs.append(output)

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

        _interactiveoptions = ['name', 'type']

        assert isinstance(
            name, str), "Error: 'name' argument should be of type string."
        assert isinstance(
            type, str), "Error: 'type' argument should be of type string."
        assert type in ['checkbox', 'input', 'integer', 'number', 'select', 'slider',
                        'display'], 'Error: Option "type" is not of standard Option interface parameter.'

        option = {}

        option['name'] = name

        if type == 'checkbox':
            option['type'] = "CheckboxOption"
            value = kwargs.get('value', False)
            assert isinstance(
                value, bool), "Error: For checkbox option, 'value' must be of type boolean."
            option['value'] = value

        elif type == 'input':
            option['type'] = "InputOption"
            value = kwargs.get('value', "Text input")
            assert isinstance(
                value, str), "Error: For input option, 'value' must be of type string."
            option['value'] = value

        elif type == 'integer':
            option['type'] = "IntegerOption"

            if 'value' in kwargs:
                value = kwargs.get('value')
                assert isinstance(
                    value, int), "Error: For checkbox option, 'value' must be of type integer."
            else:
                value = None
            option['value'] = value

            if 'min' in kwargs:
                min = kwargs.get('min')
                assert isinstance(
                    min, int), "Error: For checkbox option, 'min' must be of type integer."
            else:
                min = None
            option['min'] = min

            if 'max' in kwargs:
                max = kwargs.get('max')
                assert isinstance(
                    max, int), "Error: For checkbox option, 'max' must be of type integer."
            else:
                max = None
            option['max'] = max
            option['properties'] = {'min': min, 'max': max}

        elif type == 'number':
            option['type'] = "NumberOption"

            if 'value' in kwargs:
                value = kwargs.get('value')
                assert isinstance(value, int) or isinstance(
                    value, float), "Error: For checkbox option, 'value' must be of type float or integer."
            else:
                value = None
            option['value'] = value

            if 'min' in kwargs:
                min = kwargs.get('min')
                assert isinstance(min, int) or isinstance(
                    min, float), "Error: For checkbox option, 'min' must be of type float or integer."
            else:
                min = None
            option['min'] = min

            if 'max' in kwargs:
                max = kwargs.get('max')
                assert isinstance(max, int) or isinstance(
                    max, float), "Error: For checkbox option, 'max' must be of type float or integer."
            else:
                max = None
            option['max'] = max
            option['properties'] = {'min': min, 'max': max}

        elif type == 'select':
            option['type'] = "SelectOption"

            if 'value' in kwargs:
                value = kwargs.get('value')
                assert isinstance(
                    value, str), "Error: For select option, 'value' must be of string."
            else:
                value = None
            option['value'] = value

            items = kwargs.get('items', [])
            assert bool(
                items), "Error: There are no items specified for the select option."
            assert all(isinstance(item, str)
                       for item in items), "Error: items specified for the select option must all be of type string."
            option['items'] = items
            option['properties'] = {'items': items}

        elif type == 'slider':
            option['type'] = "SliderOption"

            if 'value' in kwargs:
                value = kwargs.get('value')
                assert isinstance(value, int) or isinstance(
                    value, float), "Error: For slider option, 'value' must be of type float or integer."
            else:
                value = None
            option['value'] = value

            min = kwargs.get('min', None)

            assert (
                min is not None), "Error: For slider option, 'min' must be specified."
            assert isinstance(min, int) or isinstance(
                min, float), "Error: For slider option, 'min' must be of type float or integer."
            option['min'] = min

            max = kwargs.get('max', None)
            assert bool(
                max), "Error: For slider option, 'max' must be specified."
            assert isinstance(max, int) or isinstance(
                max, float), "Error: For slider option, 'max' must be of type float or integer."
            option['max'] = max
            option['properties'] = {'min': min, 'max': max}

        elif type == 'display':
            option['type'] = "TextOption"
            value = kwargs.get('value', "null text")
            assert isinstance(
                value, str), "Error: For text option, 'value' must be of type string."
            option['value'] = value

        else:
            raise('Error: No valid option type passed to the addOption method.')

        self.options.append(option)

    def _export(self):
        return {'name': self.name, 'inputs': self.inputs, 'outputs': self.outputs, 'options': self.options}

    def on_calculate():
        pass

    def add_calculate(self, calcFunc: Callable):
        self.onCalculate = types.MethodType(calcFunc, self)

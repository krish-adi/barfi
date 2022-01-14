import types
from typing import Callable


class Block(object):
    """

    """

    _interfaceVariables = ['name']

    def __init__(self, **kwargs) -> None:
        # Initialise the Block object

        # To set the name of the Block, default = Block
        self.BlockName = kwargs.get('name', 'Block')

        # To set the defaults for Inputs, Outputs, Options
        self.Inputs = []
        self.Outputs = []
        self.Options = []

    def addInput(self, **kwargs) -> None:
        """
        A function defined to add an Input interface to the Block

        Use as:
            self.addInput(**kwargs)

        Interface options:
            name (str)  : The name of the Input interface.
        """

        Input = {}
        if not bool(kwargs):
            in_nos = len(self.Inputs)
            Input['name'] = 'Input ' + str(in_nos + 1)
        else:
            for arg in kwargs:
                if arg not in list(self._interfaceVariables):
                    raise(
                        'Error: Argument passed not in the list of Input interface parameters.')
                arg_val = kwargs.get(arg)
                Input[arg] = arg_val

        self.Inputs.append(Input)

    def addOutput(self, **kwargs) -> None:
        """
        A function defined to add an Output interface to the Block

        Use as:
            self.addOutput(**kwargs)

        Interface options:
            name (str)  : The name of the Output interface.
        """

        Output = {}
        if not bool(kwargs):
            in_nos = len(self.Outputs)
            Output['name'] = 'Output ' + str(in_nos + 1)
        else:
            for arg in kwargs:
                if arg not in list(self._interfaceVariables):
                    raise(
                        'Error: Argument passed not in the list of Input interface parameters.')
                arg_val = kwargs.get(arg)
                Output[arg] = arg_val

        self.Outputs.append(Output)

    def addOption(self, name: str, type: str, **kwargs) -> None:
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

        _interactiveOptions = ['name', 'type']

        assert isinstance(
            name, str), "Error: 'name' argument should be of type string."
        assert isinstance(
            type, str), "Error: 'type' argument should be of type string."
        assert type in ['checkbox', 'input', 'integer', 'number', 'select', 'slider',
                        'display'], 'Error: Option "type" is not of standard Option interface parameter.'

        Option = {}

        Option['name'] = name

        if type == 'checkbox':
            Option['type'] = "CheckboxOption"
            value = kwargs.get('value', False)
            assert isinstance(
                value, bool), "Error: For checkbox option, 'value' must be of type boolean."
            Option['value'] = value

        elif type == 'input':
            Option['type'] = "InputOption"
            value = kwargs.get('value', "Text input")
            assert isinstance(
                value, str), "Error: For input option, 'value' must be of type string."
            Option['value'] = value

        elif type == 'integer':
            Option['type'] = "IntegerOption"

            if 'value' in kwargs:
                value = kwargs.get('value')
                assert isinstance(
                    value, int), "Error: For checkbox option, 'value' must be of type integer."
            else:
                value = None
            Option['value'] = value

            if 'min' in kwargs:
                min = kwargs.get('min')
                assert isinstance(
                    min, int), "Error: For checkbox option, 'min' must be of type integer."
            else:
                min = None
            Option['min'] = min

            if 'max' in kwargs:
                max = kwargs.get('max')
                assert isinstance(
                    max, int), "Error: For checkbox option, 'max' must be of type integer."
            else:
                max = None
            Option['max'] = max
            Option['properties'] = {'min': min, 'max': max}

        elif type == 'number':
            Option['type'] = "NumberOption"

            if 'value' in kwargs:
                value = kwargs.get('value')
                assert isinstance(value, int) or isinstance(
                    value, float), "Error: For checkbox option, 'value' must be of type float or integer."
            else:
                value = None
            Option['value'] = value

            if 'min' in kwargs:
                min = kwargs.get('min')
                assert isinstance(min, int) or isinstance(
                    min, float), "Error: For checkbox option, 'min' must be of type float or integer."
            else:
                min = None
            Option['min'] = min

            if 'max' in kwargs:
                max = kwargs.get('max')
                assert isinstance(max, int) or isinstance(
                    max, float), "Error: For checkbox option, 'max' must be of type float or integer."
            else:
                max = None
            Option['max'] = max
            Option['properties'] = {'min': min, 'max': max}

        elif type == 'select':
            Option['type'] = "SelectOption"

            if 'value' in kwargs:
                value = kwargs.get('value')
                assert isinstance(
                    value, str), "Error: For select option, 'value' must be of string."
            else:
                value = None
            Option['value'] = value

            items = kwargs.get('items', [])
            assert bool(
                items), "Error: There are no items specified for the select option."
            assert all(isinstance(item, str)
                       for item in items), "Error: items specified for the select option must all be of type string."
            Option['items'] = items
            Option['properties'] = {'items': items}

        elif type == 'slider':
            Option['type'] = "SliderOption"

            if 'value' in kwargs:
                value = kwargs.get('value')
                assert isinstance(value, int) or isinstance(
                    value, float), "Error: For slider option, 'value' must be of type float or integer."
            else:
                value = None
            Option['value'] = value

            min = kwargs.get('min', None)
            print(bool(min))

            assert (
                min is not None), "Error: For slider option, 'min' must be specified."
            assert isinstance(min, int) or isinstance(
                min, float), "Error: For slider option, 'min' must be of type float or integer."
            Option['min'] = min

            max = kwargs.get('max', None)
            assert bool(
                max), "Error: For slider option, 'max' must be specified."
            assert isinstance(max, int) or isinstance(
                max, float), "Error: For slider option, 'max' must be of type float or integer."
            Option['max'] = max
            Option['properties'] = {'min': min, 'max': max}
            
        elif type == 'display':
            Option['type'] = "TextOption"
            value = kwargs.get('value', "null text")
            assert isinstance(
                value, str), "Error: For text option, 'value' must be of type string."
            Option['value'] = value

        else:
            raise('Error: No valid option type passed to the addOption method.')

        self.Options.append(Option)

    def _export(self):
        return {'Name': self.BlockName, 'Inputs': self.Inputs, 'Outputs': self.Outputs, 'Options': self.Options}

    def onCalculate():
        pass

    def addCalculate(self, calcFunc: Callable):
        self.onCalculate = types.MethodType(calcFunc, self)

import types
from typing import Callable
from .option_builder import build_option


class Block(object):

    def __init__(self, name: str = 'Block') -> None:
        # Initialise the Block object

        # To set the name of the Block, default = Block
        # Reference to the type of the Block
        self._type = name
        # Title of the block on the editor
        self._name = name

        # To set the defaults for inputs, outputs, options
        self._inputs = {}
        self._outputs = {}
        self._options = []

    def __repr__(self) -> str:
        return f'<barfi.Block of type `{self._type}` at {hex(id(self))}>'

    def __str__(self) -> str:        
        inputs_name = [input['name'] for input in self._inputs]
        outputs_name = [output['name'] for output in self._outputs]
        options_name = [option['name'] for option in self._options]
        line_1 = f'barfi.Block of type {self._type} with name {self._name} \n'
        line_2 = f'Inputs: {inputs_name!r} \n'
        line_3 = f'Outputs: {outputs_name!r} \n'
        line_4 = f'Options: {options_name!r} '
        return line_1 + line_2 + line_3 + line_4

    def add_input(self, name: str = None, value = None) -> None:
        """
        A function defined to add an Input interface to the Block

        Use as:
            self.addInput(name='Input Name')

        Interface options:
            name (str)  : The name of the Input interface.
            value (any)  : The default value for this input interface.
        """
        # TODO check if name already does not exist in outputs and inputs, 
        # raise value error, must be unique for input and output
        if name:
            self._inputs[name] = {'value': value, 'id': None}
        else:
            in_nos = len(self._inputs)
            input_name = 'Input ' + str(in_nos + 1)
            self._inputs[input_name] = {'value': value, 'id': None}

    def add_output(self, name: str = None, value = None) -> None:
        """
        A function defined to add an Output interface to the Block

        Use as:
            self.addOutput(name='Output Name')

        Interface options:
            name (str)  : The name of the Output interface.
            value (any)  : The default value for this output interface.
        """
        # TODO check if name already does not exist in outputs and inputs, 
        # raise value error, must be unique for input and output
        if name:
            self._outputs[name] = {'value': value, 'id': None}
        else:
            out_nos = len(self._outputs)
            output_name = 'Output ' + str(out_nos + 1)
            self._outputs[output_name] = {'value': value, 'id': None}

    def _add_option(self, name: str, type: str, **kwargs) -> None:
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
        _inputs_export = []
        _outputs_export = []
        for key, _ in self._inputs.items():
            _inputs_export.append({'name': key})
        for key, _ in self._outputs.items():
            _outputs_export.append({'name': key})

        return {'name': self._name, 'inputs': _inputs_export, 'outputs': _outputs_export, 'options': self._options}

    def get_interface(self, name: str):
        
        if name in self._inputs:
            return self._inputs[name]['value']  
        elif name in self._outputs:
            return self._outputs[name]['value']    
        else:
            return None    

    def set_interface(self, name: str, **kwargs) -> None:
        if name in self._inputs:
            for arg, value in kwargs.items():
                if arg in ['value', 'id']:
                    self._inputs[name][arg] = value
                else:
                    raise ValueError
        elif name in self._outputs:
            for arg, value in kwargs.items():
                if arg in ['value', 'id']:
                    self._outputs[name][arg] = value
                else:
                    raise ValueError        

    def _on_compute():
        pass

    def add_compute(self, _func: Callable):
        self._on_compute = types.MethodType(_func, self)

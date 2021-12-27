import types

class Block(object):
    """

    """

    _interfaceVariables = ['name']

    def __init__(self, **kwargs):
        # Initialise the Block object

        # To set the name of the Block, default = Block
        self.BlockName = kwargs.get('name', 'Block')

        # To set the defaults for Inputs, Outputs, Options
        self.InputsInfo = []
        self.OutputsInfo = []
        self.OptionsInfo = []

    def addInput(self, **kwargs):
        """
        A function defined to add an Input interface to the Block

        Use as:
            self.addInput(**kwargs)

        Interface options:
            name = ""
        """

        Input = {}
        if not bool(kwargs):
            in_nos = len(self.InputsInfo)
            Input['name'] = 'Input ' + str(in_nos + 1)
        else:
            for arg in kwargs:
                if arg not in list(self._interfaceVariables):
                    raise(
                        'Error: Argument passed not in the list of Input interface parameters.')
                arg_val = kwargs.get(arg)
                Input[arg] = arg_val

        self.InputsInfo.append(Input)

    def addOutput(self, **kwargs):
        """
        A function defined to add an Output interface to the Block

        Use as:
            self.addOutput(**kwargs)

        Interface options:
            name = ""
        """

        Output = {}
        if not bool(kwargs):
            in_nos = len(self.OutputsInfo)
            Output['name'] = 'Output ' + str(in_nos + 1)
        else:
            for arg in kwargs:
                if arg not in list(self._interfaceVariables):
                    raise(
                        'Error: Argument passed not in the list of Input interface parameters.')
                arg_val = kwargs.get(arg)
                Output[arg] = arg_val

        self.OutputsInfo.append(Output)

    def onCalculate():
        pass 

    def addCalculate(self, calcFunc):
        self.onCalculate = types.MethodType( calcFunc, self )

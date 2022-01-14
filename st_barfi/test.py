import block as bb

feed = bb.Block(name='Feed')
feed.addOutput()

splitter = bb.Block(name='Splitter')
splitter.addInput()
splitter.addOutput()
splitter.addOutput()
splitter.addOption(name='a-checkbox-option', type='checkbox', value=True)

mixer = bb.Block(name='Mixer')
mixer.addInput()
mixer.addInput()
mixer.addOutput()

result = bb.Block(name='Result')
result.addInput()

blocks = [feed, splitter, mixer, result]


def calcFunc(self):
    print(self.BlockName)


feed.addCalculate(calcFunc)

feed.onCalculate()

# feed = {'Name': 'Feed',
#         'InputsInfo': [],
#         'OutputsInfo': [{'name': 'Output'}]}
# splitter = {'Name': 'Splitter',
#             'InputsInfo': [{'name': 'Input'}],
#             'OutputsInfo': [{'name': 'Output 1'}, {'name': 'Output 2'}]}
# mixer = {'Name': 'Mixer',
#          'InputsInfo': [{'name': 'Input 1'}, {'name': 'Input 2'}],
#          'OutputsInfo': [{'name': 'Output'}]}
# result = {'Name': 'Result',
#           'InputsInfo': [{'name': 'Input'}],
#           'OutputsInfo': []}


# blocks = [feed, splitter, mixer, result]
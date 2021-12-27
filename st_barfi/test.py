import block as bb

feed = bb.Block(name='Feed')
feed.addOutput()

splitter = bb.Block(name='Splitter')
splitter.addInput()
splitter.addOutput()
splitter.addOutput()

mixer = bb.Block(name='Mixer')
mixer.addInput()
mixer.addInput()
mixer.addOutput()

result = bb.Block(name='Result')
result.addInput()

blocks = [feed, splitter, mixer, result]

def calcFunc( self ):
    print(self.BlockName)

feed.addCalculate(calcFunc)

feed.onCalculate()
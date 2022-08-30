from tkinter.tix import Select

from soupsieve import select
from barfi import Block

feed = Block(name='Feed')
feed.add_output()
def feed_func(self):
    self.set_interface(name='Output 1', value=4)
feed.add_compute(feed_func)

splitter = Block(name='Splitter')
splitter.add_input()
splitter.add_output()
splitter.add_output()
def splitter_func(self):
    in_1 = self.get_interface(name='Input 1')
    value = (in_1/2)
    self.set_interface(name='Output 1', value=value)
    self.set_interface(name='Output 2', value=value)
splitter.add_compute(splitter_func)

mixer = Block(name='Mixer')
mixer.add_input()
mixer.add_input()
mixer.add_output()
def mixer_func(self):    
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = (in_1 + in_2)
    self.set_interface(name='Output 1', value=value)
mixer.add_compute(mixer_func)

result = Block(name='Result')
result.add_input()
def result_func(self):
    in_1 = self.get_interface(name='Input 1')
result.add_compute(result_func)

checkbox = Block(name='Checkbox')
checkbox.add_output()
checkbox.add_option(name='display-option', type='display', value='This is a Block with Checkbox option.')
checkbox.add_option(name='checkbox-option', type='checkbox')

input = Block(name='Input')
input.add_output()
input.add_option(name='display-option', type='display', value='This is a Block with Input option.')
input.add_option(name='input-option', type='input')

integer = Block(name='Integer')
integer.add_output()
integer.add_option(name='display-option', type='display', value='This is a Block with Integer option.')
integer.add_option(name='integer-option', type='integer')

number = Block(name='Number')
number.add_output()
number.add_option(name='display-option', type='display', value='This is a Block with Number option.')
number.add_option(name='number-option', type='number')

selecto = Block(name='Select')
selecto.add_output()
selecto.add_option(name='display-option', type='display', value='This is a Block with Select option.')
selecto.add_option(name='select-option', type='select', items=['Select A', 'Select B', 'Select C'])

slider = Block(name='Slider')
slider.add_output()
slider.add_option(name='display-option', type='display', value='This is a Block with Slider option.')
slider.add_option(name='slider-option', type='slider', min=0, max=10)

base_blocks = [feed, result, mixer, splitter, checkbox, input, integer, number, selecto, slider]
base_blocks_category = {'process': [feed, result, mixer, splitter], 'options':[checkbox, input, integer, number, selecto, slider]}

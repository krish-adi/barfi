from barfi.flow import Block


def number_10_func(self):
    self.set_interface(name="Output 1", value=10)
    print(self.get_interface(name="Output 1"))


number_10 = Block(name="Number 10")
number_10.add_output()
number_10.add_compute(number_10_func)


def number_5_func(self):
    self.set_interface(name="Output 1", value=5)
    print(self.get_interface(name="Output 1"))


number_5 = Block(name="Number 5")
number_5.add_output()
number_5.add_compute(number_5_func)


def real_number_func(self):
    option_value = self.get_option(name="number-option")
    self.set_interface(name="Output 1", value=option_value)
    print(self.get_interface(name="Output 1"))


real_number = Block(name="Real Number")
real_number.add_output()
real_number.add_option(
    name="display-option", type="display", value="This is a Block with Number option."
)
real_number.add_option(name="number-option", type="number")
real_number.add_compute(real_number_func)


def subtraction_func(self):
    print("subtraction_func")
    in_1 = self.get_interface(name="Input 1")
    in_2 = self.get_interface(name="Input 2")
    value = in_1 - in_2
    print(f"{in_1} - {in_2} = {value}")
    self.set_interface(name="Output 1", value=value)


subtraction = Block(name="Subtraction")
subtraction.add_input()
subtraction.add_input()
subtraction.add_output()
subtraction.add_compute(subtraction_func)


def addition_func(self):
    print("addition_func")
    in_1 = self.get_interface(name="Input 1")
    in_2 = self.get_interface(name="Input 2")
    value = in_1 + in_2
    print(f"{in_1} + {in_2} = {value}")
    self.set_interface(name="Output 1", value=value)


addition = Block(name="Addition")
addition.add_input()
addition.add_input()
addition.add_output()
addition.add_compute(addition_func)


def multiplication_func(self):
    print("multiplication_func")
    in_1 = self.get_interface(name="Input 1")
    in_2 = self.get_interface(name="Input 2")
    value = in_1 * in_2
    print(f"{in_1} * {in_2} = {value}")
    self.set_interface(name="Output 1", value=value)


multiplication = Block(name="Multiplication")
multiplication.add_input()
multiplication.add_input()
multiplication.add_output()
multiplication.add_compute(multiplication_func)


def division_func(self):
    print("division_func")
    in_1 = self.get_interface(name="Input 1")
    in_2 = self.get_interface(name="Input 2")
    value = in_1 / in_2
    print(f"{in_1} / {in_2} = {value}")
    self.set_interface(name="Output 1", value=value)


division = Block(name="Division")
division.add_input()
division.add_input()
division.add_output()
division.add_compute(division_func)


checkbox = Block(name="Checkbox")
checkbox.add_input()
checkbox.add_output()
checkbox.add_option(
    name="display-option", type="display", value="This is a Block with Checkbox option."
)
checkbox.add_option(name="checkbox-option", type="checkbox")

input = Block(name="Input")
input.add_output()
input.add_option(
    name="display-option", type="display", value="This is a Block with Input option."
)
input.add_option(name="input-option", type="input")

integer = Block(name="Integer")
integer.add_output()
integer.add_option(
    name="display-option", type="display", value="This is a Block with Integer option."
)
integer.add_option(name="integer-option", type="integer")

number = Block(name="Number")
number.add_output()
number.add_option(
    name="display-option", type="display", value="This is a Block with Number option."
)
number.add_option(name="number-option", type="number")

selecto = Block(name="Select")
selecto.add_input()
selecto.add_output()
selecto.add_option(
    name="display-option", type="display", value="This is a Block with Select option."
)
selecto.add_option(
    name="select-option", type="select", items=["Select A", "Select B", "Select C"]
)

slider = Block(name="Slider")
slider.add_input()
slider.add_output()
slider.add_option(
    name="display-option", type="display", value="This is a Block with Slider option."
)
slider.add_option(name="slider-option", type="slider", min=0, max=10)


def feed_func(self):
    self.set_interface(name="Output 1", value=4)


feed = Block(name="Feed")
feed.add_output()
feed.add_compute(feed_func)


def splitter_func(self):
    in_1 = self.get_interface(name="Input 1")
    value = in_1 / 2
    self.set_interface(name="Output 1", value=value)
    self.set_interface(name="Output 2", value=value)


splitter = Block(name="Splitter")
splitter.add_input()
splitter.add_output()
splitter.add_output()
splitter.add_compute(splitter_func)


def mixer_func(self):
    in_1 = self.get_interface(name="Input 1")
    in_2 = self.get_interface(name="Input 2")
    value = in_1 + in_2
    self.set_interface(name="Output 1", value=value)


mixer = Block(name="Mixer")
mixer.add_input()
mixer.add_input()
mixer.add_output()
mixer.add_compute(mixer_func)

three_mixer = Block(name="Three Mixer")
three_mixer.add_input()
three_mixer.add_input()
three_mixer.add_input()
three_mixer.add_output()


def result_func(self):
    value = self.get_interface(name="Input 1")
    print(value)


result = Block(name="Result")
result.add_input()
result.add_compute(result_func)

process_blocks = [feed, mixer, splitter]

options_blocks = [input, integer, number, checkbox, selecto, slider, three_mixer]

math_blocks = [
    # number_10,
    # number_5,
    real_number,
    result,
    addition,
    subtraction,
    multiplication,
    division,
]

base_blocks = {
    "Math": math_blocks,
    "Process": process_blocks,
    "Options": options_blocks,
}

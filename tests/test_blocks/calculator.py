from barfi import Block

number_10 = Block(name='Number')
number_10.add_output()


def number_10_func(self):
    self.set_interface(name='Output 1', value=10)


number_10.add_compute(number_10_func)

number_5 = Block(name='Number')
number_5.add_output()


def number_5_func(self):
    self.set_interface(name='Output 1', value=5)


number_5.add_compute(number_5_func)

subtraction = Block(name='Subtraction')
subtraction.add_input()
subtraction.add_input()
subtraction.add_output()


def subtraction_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = in_1 - in_2
    self.set_interface(name='Output 1', value=value)


subtraction.add_compute(subtraction_func)

addition = Block(name='Addition')
addition.add_input()
addition.add_input()
addition.add_output()


def addition_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = in_1 + in_2
    self.set_interface(name='Output 1', value=value)


addition.add_compute(addition_func)

multiplication = Block(name='Multiplication')
multiplication.add_input()
multiplication.add_input()
multiplication.add_output()


def multiplication_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = in_1 * in_2
    self.set_interface(name='Output 1', value=value)


multiplication.add_compute(multiplication_func)

division = Block(name='Division')
division.add_input()
division.add_input()
division.add_output()
division.add_option(name='checkbox_1', type='checkbox')
division.add_option(name='input_1', type='input')
division.add_option(name='integer_1', type='integer')
division.add_option(name='number_1', type='number')
division.add_option(name='select_1', type='select', items=['item_1', 'item_2'])
division.add_option(name='slider_1', type='slider', min=0, max=10)
division.add_option(name='display_1', type='display')


def division_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = in_1 / in_2
    self.set_interface(name='Output 1', value=value)


division.add_compute(division_func)

result = Block(name='Result')
result.add_input()


def result_func(self):
    in_1 = self.get_interface(name='Input 1')
    print(in_1)


result.add_compute(result_func)

math_blocks = [number_10, number_5, result,
               addition, subtraction, multiplication, division]

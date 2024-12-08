from barfi.st_flow import Block


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


def subtraction_func(self):
    print("subtraction_func")
    in_1 = self.get_interface(name="Input 1")
    in_2 = self.get_interface(name="Input 2")
    value = in_1 - in_2
    self.set_interface(name="Output 1", value=value)


subtraction = Block(name="Subtraction")
subtraction.add_input()
subtraction.add_input()
subtraction.add_output()
subtraction.add_compute(subtraction_func)


def addition_func(self):
    print("addition_func")
    in_1 = self.get_interface(name="Input 1")
    print(in_1)
    in_2 = self.get_interface(name="Input 2")
    print(in_2)
    value = in_1 + in_2
    self.set_interface(name="Output 1", value=value)
    print(value)
    print(self.get_interface(name="Output 1"))


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
    self.set_interface(name="Output 1", value=value)


division = Block(name="Division")
division.add_input()
division.add_input()
division.add_output()
division.add_compute(division_func)


def result_func(self):
    _ = self.get_interface(name="Input 1")


result = Block(name="Result")
result.add_input()
result.add_compute(result_func)

math_blocks = [
    number_10,
    number_5,
    result,
    addition,
    subtraction,
    multiplication,
    division,
]

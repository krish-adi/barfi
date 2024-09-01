from barfi import Block

checkbox = Block(name="Checkbox")
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
selecto.add_output()
selecto.add_option(
    name="display-option", type="display", value="This is a Block with Select option."
)
selecto.add_option(
    name="select-option", type="select", items=["Select A", "Select B", "Select C"]
)

slider = Block(name="Slider")
slider.add_output()
slider.add_option(
    name="display-option", type="display", value="This is a Block with Slider option."
)
slider.add_option(name="slider-option", type="slider", min=0, max=10)

options_blocks = [checkbox, input, integer, number, selecto, slider]

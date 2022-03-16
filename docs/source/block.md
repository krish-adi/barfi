# Block

A *Block* is the fundamental part of the flow based programming philosophy of *barfi*. It can be considered as the building block that is used to build the data flow program. A *Block* has inputs, outputs and performs some computation. Any number of inputs and outputs can be added. Inputs and outputs are considered to be the interface to the *Block*, a connection. The inputs and outputs make up the connections to the other *Blocks* in the visual interface (the editor). The computation that each *Block* is to perform is to be specified when building the *Block*. When bluiding a *Block*, you only build a fundamental base *Block*. It is then considered that multiples/copies of these base *Block* are used to build the data flow.

__Add picture of the block and the schema.__

As a comparison to the common *Node* based programming, a *Node* is generally considered to perform a single specific computation. With *barfi*, a *Block* is considered to perform any type of computation, simple or complex.

## Building a *Block*

A *Block* here is a Python class object. That is built using the *Block* class in *barfi*. 

```python
from barfi import Block
```

Create your fundamental *Block* by giving it a name as:

```python
my_block = Block(name='My Block')
```

Add an input interface to your *Block*, `my_block` as:

```python
my_block.add_input()
```

This creates an input interface with name `Input 1`, `Input 2`, and so. But if would like to add an input interface with a given name, use:

```python
my_block.add_input(name='my input')
```

And, similarly you can add an output as:

```python
my_block.add_output() # Creates an output with name: 'Output 1'
my_block.add_output(name='my output') # Creates an output with name: 'my output'
```

**Adding a compute function to the *Block***

The idea of building a flow based program is to perform repeated computations using *Blocks*, and to customize the flow/program with the addition and/or removal of *Blocks*. Connections between the *Blocks* direct to how the program is executed and how data flows. 

To add the computation function (ex. `my_block_func`) to your *Block*, make use of:

```python
my_block.add_compute(my_block_func)
```

To execute this, you need to define your compute function (`my_block_func`). You need to pass in the argument `self`, as this function will be added as a method of your *Block* class. You can **access/get** the input interface values using `self.get_interface(name='my input')` with the name of the input. You can **set** the output interface values using `self.set_interface(name= 'my output', value= my_output_value)` with the `name` of the output interface and the `value` to be set.

```python
def my_block_func(self):
    # get the value of the input interface
    in_1 = self.get_interface(name='input_1') 
    
    out_1 = (in_1/2) # ... perform come computation

    # get the value of the output interface
    self.set_interface(name='output_1', value=out_1) 
```
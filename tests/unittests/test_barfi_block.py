import unittest
from barfi import Block
import sys
sys.path.append('../../')


class TestBarfiBlock(unittest.TestCase):

    def setUp(self):
        pass

    def test_block_name(self):
        block_1 = Block()
        block_2 = Block(name='BlockName')
        self.assertEqual(block_1._type, 'Block')
        self.assertEqual(block_1._name, 'Block')
        self.assertEqual(block_2._type, 'BlockName')
        self.assertEqual(block_2._name, 'BlockName')

    def test_block_inputs(self):
        block_1 = Block()
        block_1.add_input()
        self.assertEqual(block_1._inputs, {
                         'Input 1': {'value': None, 'id': None}})
        block_1.add_input(name='some input')
        self.assertEqual(block_1._inputs, {'Input 1': {
                         'value': None, 'id': None}, 'some input': {'value': None, 'id': None}})
        # TODO check for value error for existing name

    def test_block_outputs(self):
        block_1 = Block()
        block_1.add_output()
        self.assertEqual(block_1._outputs, {
                         'Output 1': {'value': None, 'id': None}})
        block_1.add_output(name='some output')
        self.assertEqual(block_1._outputs, {'Output 1': {
                         'value': None, 'id': None}, 'some output': {'value': None, 'id': None}})
        # TODO check for value error for existing name

    def test_block_options(self):
        # TODO After the implementation of options
        pass

    def test_set_interface(self):
        block_1 = Block()
        block_1.add_input()
        block_1.set_interface(name='Input 1', value=5)
        self.assertEqual(block_1._inputs, {
                         'Input 1': {'value': 5, 'id': None}})
        block_1.set_interface(name='Input 1', id=123456)
        self.assertEqual(block_1._inputs, {
                         'Input 1': {'value': 5, 'id': 123456}})
        block_1.add_output()
        block_1.set_interface(name='Output 1', value=5)
        self.assertEqual(block_1._outputs, {
                         'Output 1': {'value': 5, 'id': None}})
        block_1.set_interface(name='Output 1', id=123456)
        self.assertEqual(block_1._outputs, {
                         'Output 1': {'value': 5, 'id': 123456}})
        # TODO check ValueError for not in ['value', 'id']

    def test_get_interface(self):
        block_1 = Block()
        block_1.add_input()
        block_1.set_interface(name='Input 1', value=5)
        self.assertEqual(block_1.get_interface(name='Input 1'), 5)

    def test_block_calculate(self):
        block_1 = Block(name='block_1')
        block_1.add_input(name='input_1')
        block_1.add_output(name='output_1')
        block_1.set_interface(name='input_1', value=5)

        def block_1_func(self):
            in_1 = self.get_interface(name='input_1')
            out_1 = (in_1/2)
            self.set_interface(name='output_1', value=out_1)
        block_1.add_calculate(block_1_func)
        block_1._on_calculate()
        self.assertEqual(block_1.get_interface(name='input_1'), 5)
        self.assertEqual(block_1.get_interface(name='output_1'), 2.5)


if __name__ == '__main__':
    unittest.main()

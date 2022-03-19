import sys
sys.path.append('../../')
from barfi import Block
import unittest

class TestBarfiBlock(unittest.TestCase):

    def setUp(self):
        pass

    def test_block_option_checkbox(self):
        block_1 = Block()
        block_1.add_option(name='checkbox-option-1', type='checkbox')
        self.assertEqual(block_1._options, {
                         'checkbox-option-1': {'name': 'checkbox-option-1', 'type': 'CheckboxOption', 'value': False}})
        with self.assertRaises(ValueError):
            block_1.add_option(name='checkbox-option-1', type='checkbox')
        block_1.add_option(name='checkbox-option-2', type='checkbox')
        self.assertEqual(block_1._options, {
                         'checkbox-option-1': {'name': 'checkbox-option-1', 'type': 'CheckboxOption', 'value': False},
                         'checkbox-option-2': {'name': 'checkbox-option-2', 'type': 'CheckboxOption', 'value': False}})

    def test_block_option_set(self):
        block_1 = Block()
        block_1.add_option(name='checkbox-option-1', type='checkbox')
        block_1.set_option(name='checkbox-option-1', value=True)
        self.assertEqual(block_1._options, {
                         'checkbox-option-1': {'name': 'checkbox-option-1', 'type': 'CheckboxOption', 'value': True}})
        with self.assertRaises(ValueError):
            block_1.set_option(name='checkbox-option-1', type=True)

    def test_block_option_get(self):
        block_1 = Block()
        block_1.add_option(name='checkbox-option-1', type='checkbox')        
        self.assertEqual(block_1.get_option(name='checkbox-option-1'), False)
        block_1.set_option(name='checkbox-option-1', value=True)
        self.assertEqual(block_1.get_option(name='checkbox-option-1'), True)

    def test_block_compute_with_option(self):
        block_1 = Block(name='block_1')
        block_1.add_input(name='input_1')
        block_1.add_output(name='output_1')
        block_1.set_interface(name='input_1', value=5)
        block_1.add_option(name='checkbox-option-1', type='checkbox')                
        def block_1_func(self):
            in_1 = self.get_interface(name='input_1')
            if (self.get_option(name='checkbox-option-1')):
                out_1 = (in_1/2)
            else:
                out_1 = (in_1*2)
            self.set_interface(name='output_1', value=out_1)
        block_1.add_compute(block_1_func)
        block_1._on_compute()
        self.assertEqual(block_1.get_interface(name='input_1'), 5)
        self.assertEqual(block_1.get_interface(name='output_1'), 10)
        block_1.set_option(name='checkbox-option-1', value=True)
        block_1._on_compute()
        self.assertEqual(block_1.get_interface(name='output_1'), 2.5)

    # TODO rest of the Block options test
    #     block_1.add_option(name='input-option', type='input')
    #     block_1.add_option(name='integer-option', type='integer')
    #     block_1.add_option(name='number-option', type='number')
    #     block_1.add_option(name='select-option', type='select', items=['Select A', 'Select B', 'Select C'])
    #     block_1.add_option(name='slider-option', type='slider', min=0, max=10)
    #     block_1.add_option(name='display-option', type='display', value='Here some text that can be displayed in the Block.')
    
if __name__ == '__main__':
    unittest.main()

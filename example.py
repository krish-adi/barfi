feed = Block(name='Feed')
feed.add_output()
feed.add_output()
feed.add_option(name='a-check-box-option', type='checkbox', value=True)
feed.add_option(name='a-text-input-option',
               type='input', value="enter text here")
feed.add_option(name='an-integer-intput-option',
               type='integer', value=5, min=1, max=10)
feed.add_option(name='a-number-intput-option',
               type='number', value=2.5, min=0, max=5)
feed.add_option(name='a-select-item-option', type='select',
               value='item 1', items=['item 1', 'item 2', 'item 3'])
feed.add_option(name='a-slider-option', type='slider', value=5, min = 0, max=10)
feed.add_option(name='a-display-option', type='display',
               value='some text to be displayed here.')
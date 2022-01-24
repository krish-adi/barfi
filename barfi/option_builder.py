def build_option(name: str, type: str, kwargs):
    option = {}

    option['name'] = name

    if type == 'checkbox':
        option['type'] = "CheckboxOption"
        value = kwargs.get('value', False)
        assert isinstance(
            value, bool), "Error: For checkbox option, 'value' must be of type boolean."
        option['value'] = value

    elif type == 'input':
        option['type'] = "InputOption"
        value = kwargs.get('value', "Text input")
        assert isinstance(
            value, str), "Error: For input option, 'value' must be of type string."
        option['value'] = value

    elif type == 'integer':
        option['type'] = "IntegerOption"

        if 'value' in kwargs:
            value = kwargs.get('value')
            assert isinstance(
                value, int), "Error: For checkbox option, 'value' must be of type integer."
        else:
            value = None
        option['value'] = value

        if 'min' in kwargs:
            min = kwargs.get('min')
            assert isinstance(
                min, int), "Error: For checkbox option, 'min' must be of type integer."
        else:
            min = None
        option['min'] = min

        if 'max' in kwargs:
            max = kwargs.get('max')
            assert isinstance(
                max, int), "Error: For checkbox option, 'max' must be of type integer."
        else:
            max = None
        option['max'] = max
        option['properties'] = {'min': min, 'max': max}

    elif type == 'number':
        option['type'] = "NumberOption"

        if 'value' in kwargs:
            value = kwargs.get('value')
            assert isinstance(value, int) or isinstance(
                value, float), "Error: For checkbox option, 'value' must be of type float or integer."
        else:
            value = None
        option['value'] = value

        if 'min' in kwargs:
            min = kwargs.get('min')
            assert isinstance(min, int) or isinstance(
                min, float), "Error: For checkbox option, 'min' must be of type float or integer."
        else:
            min = None
        option['min'] = min

        if 'max' in kwargs:
            max = kwargs.get('max')
            assert isinstance(max, int) or isinstance(
                max, float), "Error: For checkbox option, 'max' must be of type float or integer."
        else:
            max = None
        option['max'] = max
        option['properties'] = {'min': min, 'max': max}

    elif type == 'select':
        option['type'] = "SelectOption"

        if 'value' in kwargs:
            value = kwargs.get('value')
            assert isinstance(
                value, str), "Error: For select option, 'value' must be of string."
        else:
            value = None
        option['value'] = value

        items = kwargs.get('items', [])
        assert bool(
            items), "Error: There are no items specified for the select option."
        assert all(isinstance(item, str)
                    for item in items), "Error: items specified for the select option must all be of type string."
        option['items'] = items
        option['properties'] = {'items': items}

    elif type == 'slider':
        option['type'] = "SliderOption"

        if 'value' in kwargs:
            value = kwargs.get('value')
            assert isinstance(value, int) or isinstance(
                value, float), "Error: For slider option, 'value' must be of type float or integer."
        else:
            value = None
        option['value'] = value

        min = kwargs.get('min', None)

        assert (
            min is not None), "Error: For slider option, 'min' must be specified."
        assert isinstance(min, int) or isinstance(
            min, float), "Error: For slider option, 'min' must be of type float or integer."
        option['min'] = min

        max = kwargs.get('max', None)
        assert bool(
            max), "Error: For slider option, 'max' must be specified."
        assert isinstance(max, int) or isinstance(
            max, float), "Error: For slider option, 'max' must be of type float or integer."
        option['max'] = max
        option['properties'] = {'min': min, 'max': max}

    elif type == 'display':
        option['type'] = "TextOption"
        value = kwargs.get('value', "null text")
        assert isinstance(
            value, str), "Error: For text option, 'value' must be of type string."
        option['value'] = value

    else:
        raise('Error: No valid option type passed to the addOption method.')

    return option

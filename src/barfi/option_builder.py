from barfi.std_types import BlockOption


def build_option(name: str, type: str, kwargs):
    if type == "checkbox":
        value = kwargs.get("value", False)
        assert isinstance(
            value, bool
        ), "Error: For checkbox option, 'value' must be of type boolean."
        return BlockOption(name=name, type="CheckboxOption", value=value)

    elif type == "input":
        value = kwargs.get("value", "Text input")
        assert isinstance(
            value, str
        ), "Error: For input option, 'value' must be of type string."
        return BlockOption(name=name, type="InputOption", value=value)

    elif type == "integer":
        value = kwargs.get("value")
        min_val = kwargs.get("min")
        max_val = kwargs.get("max")
        assert value is None or isinstance(
            value, int
        ), "Error: For integer option, 'value' must be of type integer."
        assert min_val is None or isinstance(
            min_val, int
        ), "Error: For integer option, 'min' must be of type integer."
        assert max_val is None or isinstance(
            max_val, int
        ), "Error: For integer option, 'max' must be of type integer."
        return BlockOption(
            name=name,
            type="IntegerOption",
            value=value,
            min=min_val,
            max=max_val,
            properties={"min": min_val, "max": max_val},
        )

    elif type == "number":
        value = kwargs.get("value")
        min_val = kwargs.get("min")
        max_val = kwargs.get("max")
        assert value is None or isinstance(
            value, (int, float)
        ), "Error: For number option, 'value' must be of type integer or float."
        assert min_val is None or isinstance(
            min_val, (int, float)
        ), "Error: For number option, 'min' must be of type integer or float."
        assert max_val is None or isinstance(
            max_val, (int, float)
        ), "Error: For number option, 'max' must be of type integer or float."
        return BlockOption(
            name=name,
            type="NumberOption",
            value=value,
            min=min_val,
            max=max_val,
            properties={"min": min_val, "max": max_val},
        )

    elif type == "select":
        value = kwargs.get("value")
        items = kwargs.get("items", [])
        assert bool(items), "Error: There are no items specified for the select option."
        assert all(
            isinstance(item, str) for item in items
        ), "Error: items specified for the select option must all be of type string."
        if value is not None:
            assert isinstance(
                value, str
            ), "Error: For select option, 'value' must be of type string."
            assert value in items, "Error: The selected value must be one of the items."
        return BlockOption(
            name=name,
            type="SelectOption",
            value=value,
            items=items,
            properties={"items": items},
        )

    elif type == "slider":
        value = kwargs.get("value")
        min_val = kwargs.get("min")
        max_val = kwargs.get("max")
        assert min_val is not None, "Error: For slider option, 'min' must be specified."
        assert max_val is not None, "Error: For slider option, 'max' must be specified."
        assert isinstance(
            min_val, (int, float)
        ), "Error: For slider option, 'min' must be of type float or integer."
        assert isinstance(
            max_val, (int, float)
        ), "Error: For slider option, 'max' must be of type float or integer."
        if value is not None:
            assert isinstance(
                value, (int, float)
            ), "Error: For slider option, 'value' must be of type float or integer."
            assert (
                min_val <= value <= max_val
            ), "Error: For slider option, 'value' must be between 'min' and 'max'."
        return BlockOption(
            name=name,
            type="SliderOption",
            value=value,
            min=min_val,
            max=max_val,
            properties={"min": min_val, "max": max_val},
        )

    elif type == "display":
        value = kwargs.get("value", "null display")
        assert isinstance(
            value, str
        ), "Error: For display option, 'value' must be of type string."
        return BlockOption(name=name, type="TextOption", value=value)

    else:
        raise ValueError("Error: No valid option type passed to the addOption method.")

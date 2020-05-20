from typing import List, Callable


def convert_dict_values_inside_list(
    func: Callable,
    list_of_dicts: List[dict]
) -> List[dict]:
    """
    Convert dict values that are inside a list using the received function
    """
    return [
        dict([key, func(value)] for key, value in dicts.items())
        for dicts in list_of_dicts
    ]


def convert_dict_values_inside_dict(func: Callable, dicts: dict) -> dict:
    """
    Convert dict values ​​that are inside a dict using the received function
    """
    result = {}
    for _key, _value in dicts.items():
        result[_key] = {}
        for key, value in _value.items():
            result[_key].update({
                key: func(value)
            })

    return result

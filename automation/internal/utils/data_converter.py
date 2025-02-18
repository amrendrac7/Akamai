from itertools import chain, starmap
from io import BytesIO
from typing import Dict



def flatten_json(data_dict: Dict, sep: str = "."):
    """
    """

    print(data_dict)
    def unpack(parent_key, parent_value):
        """Unpack one level of nesting in json file"""
        
        # Unpack one level only
        if isinstance(parent_key, dict):
            for key, value in parent_value.items():
                key1 = parent_key + sep + key
                yield key1, value
        elif isinstance(parent_key, list):
            i = 0
            for value in parent_value:
                key2 = parent_value + sep + str(i)
                i += 1
                yield key2, value

        else:
            yield parent_key, parent_value

    
    # Keep unpacking the json until all values are atomic elements (not a dictionary or a list)
    while True:
        data_dict = dict(chain.from_iterable(starmap(unpack, data_dict.items())))
        # Terminate condition: not any value in the json file is dictionary or list
        if not any(
            isinstance(value, dict) for value in data_dict.values() and 
            not any(isinstance(value, list) for value in data_dict.values())
            ):
            break

    return data_dict
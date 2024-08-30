"""
Implement a function called get_dict_value that takes two arguments: 
    a dictionary called dct, 
    and a string called path. 
The path string represents the nested keys of the dictionary, separated by dots. 
The function should return the value at the specified path or None 
(the Python null value, not a string) if the path does not exist.

    obj = {
        "car": {
            "wheels": 2,
            "gears": 5
        }
    }

Path:
  path = "car.gears"
The function call get_dict_value(obj, "car.gears") should return 5.

"""

def get_dict_value(dct, path):
    # Split the 'path' string into individual keys based on the dot separator - generating a list
    keys = path.split(".")
    previous = None
    
    for key in keys:

        # First iteration (handling the first key in the path)
        if previous is None:
            # Try to get the value associated with the current key from the root dictionary
            if key not in dct:
                # If the key is not found, return None
                return None
            else:
                # Check if the associated value is a dictionary or a simple value
                if not isinstance(dct.get(key), dict):
                    # If it's not a dictionary, return the value (since we reached the final node)
                    return dct.get(key)
                else:
                    # If it's a dictionary, set 'previous' to the current dictionary for further exploration
                    previous = dct.get(key)
        else:
            # For subsequent iterations (nested keys), navigate through 'previous' (the current dictionary level)
            current = previous.get(key)

            # If the key does not exist in the current dictionary, return None
            if current is None:
                return None
            else:
                # If the value associated with the key is not a dictionary, return the value (we've reached the end of the path)
                if not isinstance(current, dict):
                    return current
                else:
                    # If the value is a dictionary, update 'previous' for further nested exploration
                    previous = current

# Example usage:
obj = {
    "car": {
        "wheels": 2,
        "gears": 5
    }
}

# This should return 5 since the path "car.gears" points to that value in the dictionary
print(get_dict_value(obj, "car.gears"))  # Output: 5



#############################################

def get_dict_value_improved(dct, path):
    keys = path.split(".")
    
    # Traverse the dictionary based on the keys in the path
    for key in keys:
        if not isinstance(dct, dict) or key not in dct:
            return None
        dct = dct[key]
    
    # Return the final value found at the end of the path
    return dct

# print(get_dict_value_improved(obj, "car.gears"))  # Output: 5
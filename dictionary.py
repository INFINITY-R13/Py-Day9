# Create an empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}

# Create a dictionary with initial values
dict = {
    "a": "apple",
    "b": "ball"
}
print(dict["a"])  # Output: apple

# Add more values
dict["c"] = "cat"
print(dict)  # Output: {'a': 'apple', 'b': 'ball', 'c': 'cat'}

# Nest a dictionary and a list inside another dictionary
nested_dict = {
    "first": {
        1: "one",
        2: "two"
    },
    "second": ['love', 'hate'],
    "zero": dict
}
print(nested_dict)  # Output: {'first': {1: 'one', 2: 'two'}, 'second': ['love', 'hate'], 'zero': {'a': 'apple', 'b': 'ball', 'c': 'cat'}}

# Accessing values from nested dictionary
print(nested_dict["first"])         # Output: {1: 'one', 2: 'two'}
print(nested_dict["first"][1])      # Output: one
print(nested_dict["second"][0])     # Output: love
print(nested_dict["zero"]["a"])     # Output: apple

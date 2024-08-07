# create a dictionary
empty_dict = {}
print(empty_dict)

dict = {
    "a": "apple",
    "b": "ball"
    }
print(dict["a"])

#adding more values
dict["c"] = "cat"
print(dict)

#nesting a dictionary & list in dictionary
nested_dict = {
    "first":{
        1: "one",
        2: "two"
    },
    "second": ['love', 'hate'],
    "zero": dict
}
print(nested_dict)

#print first
print(nested_dict["first"])

#print one
print(nested_dict["first"][1])

#print love
print(nested_dict["second"][0])

#print apple
print(nested_dict["zero"]["a"])





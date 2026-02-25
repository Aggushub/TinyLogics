#🐍 Python Program — Segregate List Elements by Type


# Sample list containing multiple data types
mixed_list = [10, "Aggu", 3.14, True, 42, "Tutus", False, [1, 2, 3], (4, 5), {"a": 1}, None]

# Empty lists for each type
integers = []
floats = []
strings = []
booleans = []
lists = []
tuples = []
dicts = []
none_values = []

# Loop through each element and check its type
for item in mixed_list:
    if isinstance(item, int) and not isinstance(item, bool):  # bool is subclass of int
        integers.append(item)
    elif isinstance(item, float):
        floats.append(item)
    elif isinstance(item, str):
        strings.append(item)
    elif isinstance(item, bool):
        booleans.append(item)
    elif isinstance(item, list):
        lists.append(item)
    elif isinstance(item, tuple):
        tuples.append(item)
    elif isinstance(item, dict):
        dicts.append(item)
    elif item is None:
        none_values.append(item)

# Display segregated lists
print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)
print("Booleans:", booleans)
print("Lists:", lists)
print("Tuples:", tuples)
print("Dictionaries:", dicts)
print("None Values:", none_values)

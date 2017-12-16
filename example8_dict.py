# -*- coding: utf-8 -*-
# An empty dict
a = {}

# Result: None
print a.get("abc")

# Add a value to the dict
a["abc"] = 5

# Result: 5
print a.get("abc")

# Add another value
a[16] = "A text"

# Result: A text
print a.get(16)

# The whole dict {16: 'A text', 'abc': 5}
print a


# You can add content when creating the dict
b = {"ccc": "f", 16: 165}

# You can put dicts in a list
a_list = [a, b]

# Result: [{16: 'En text', 'abc': 5}, {16: 165, 'ccc': 'f'}]
print a_list


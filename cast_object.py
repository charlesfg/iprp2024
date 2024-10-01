import ctypes

# Create an object
obj = [1, 2, 3]

print(obj) # print the id from object

# Get the id of the object (which is the memory address in CPython)
obj_id = id(obj)

print(obj_id) # print the id from object
a = obj 

obj = "<New Object> String"

print(obj) # print the id from object

# Use ctypes to access the object from its id
retrieved_obj = ctypes.cast(obj_id, ctypes.py_object).value
print(retrieved_obj)  # Output: [1, 2, 3]
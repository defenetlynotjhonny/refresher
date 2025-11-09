# --- Basic Data Types ---
integer_var: int = 42
float_var: float = 3.14
complex_var: complex = 2 + 3j
boolean_var: bool = True
string_var: str = "Hello, world!"

print("Integer:", integer_var, "| Type:", type(integer_var))
print("Float:", float_var, "| Type:", type(float_var))
print("Complex number:", complex_var, "| Type:", type(complex_var))
print("Boolean:", boolean_var, "| Type:", type(boolean_var))
print("String:", string_var, "| Type:", type(string_var))

# --- Collection Types ---
list_var: list = [1, "text", 3.14, True]
tuple_var: tuple = (10, "tuple", False)
set_var: set = {1, 2, 3, 3}
frozenset_var: frozenset = frozenset({4, 5, 6})
dict_var: dict = {"name": "Alice", "age": 30, "is_active": True}

print("\nList:", list_var, "| Type:", type(list_var))
print("Tuple:", tuple_var, "| Type:", type(tuple_var))
print("Set:", set_var, "| Type:", type(set_var))
print("Frozenset:", frozenset_var, "| Type:", type(frozenset_var))
print("Dictionary:", dict_var, "| Type:", type(dict_var))

# --- Binary and Bytes ---
bytes_var: bytes = b"byte string"
bytearray_var: bytearray = bytearray(b"mutable bytes")
memoryview_var: memoryview = memoryview(b"memory")

print("\nBytes:", bytes_var, "| Type:", type(bytes_var))
print("Bytearray:", bytearray_var, "| Type:", type(bytearray_var))
print("Memoryview (as bytes):", memoryview_var.tobytes(), "| Type:", type(memoryview_var))

# --- NoneType ---
none_var: type(None) = None
print("\nNoneType:", none_var, "| Type:", type(none_var))

# --- Range and Other Useful Built-ins ---
range_var: range = range(5)
print("\nRange:", list(range_var), "| Type:", type(range_var))

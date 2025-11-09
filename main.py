import json

def build_data_dict():
    """
    Build a dictionary containing examples of many Python data types.
    """
    integer_var = 42
    float_var = 3.14
    complex_var = str(2 + 3j)  # JSON can't store complex numbers directly
    boolean_var = True
    string_var = "Hello, world!"
    list_var = [1, "text", 3.14, True]
    tuple_var = (10, "tuple", False)
    set_var = {1, 2, 3}
    frozenset_var = frozenset({4, 5, 6})
    dict_var = {"name": "Alice", "age": 30, "is_active": True}
    bytes_var = b"byte string"
    bytearray_var = bytearray(b"mutable bytes")
    memoryview_var = memoryview(b"memory")
    none_var = None
    range_var = range(5)

    data = {
        "integer": integer_var,
        "float": float_var,
        "complex": complex_var,
        "boolean": boolean_var,
        "string": string_var,
        "list": list_var,
        "tuple": tuple_var,
        "set": list(set_var),
        "frozenset": list(frozenset_var),
        "dict": dict_var,
        "bytes": bytes_var.decode("utf-8"),
        "bytearray": bytearray_var.decode("utf-8"),
        "memoryview": memoryview_var.tobytes().decode("utf-8"),
        "none": none_var,
        "range": list(range_var)
    }

    return data


def convert_to_json_string():
    """
    Converts the data dictionary to a JSON string using json.dumps().
    Prints the JSON string and its type.
    """
    data = build_data_dict()
    json_string = json.dumps(data, indent=4)
    print("JSON String Version:")
    print(json_string)
    print("Type:", type(json_string), "\n")
    return json_string


def convert_to_json_file():
    """
    Converts the data dictionary to JSON and writes it to a file using json.dump().
    Prints confirmation and type.
    """
    data = build_data_dict()
    with open("data_output.json", "w") as file:
        json.dump(data, file, indent=4)
    print("JSON File Version written to 'data_output.json'")
    print("Type:", type(data), "\n")


def convert_back_from_json():
    """
    Reads the JSON file and reconstructs the Python data types as best as possible.
    Prints the reconstructed dictionary and shows how types were restored.
    """
    with open("data_output.json", "r") as file:
        json_data = json.load(file)

    reconstructed = {
        "integer": int(json_data["integer"]),
        "float": float(json_data["float"]),
        "complex": complex(json_data["complex"].replace(" ", "")),  # from string "(2+3j)"
        "boolean": bool(json_data["boolean"]),
        "string": str(json_data["string"]),
        "list": list(json_data["list"]),
        "tuple": tuple(json_data["tuple"]),
        "set": set(json_data["set"]),
        "frozenset": frozenset(json_data["frozenset"]),
        "dict": dict(json_data["dict"]),
        "bytes": bytes(json_data["bytes"], "utf-8"),
        "bytearray": bytearray(json_data["bytearray"], "utf-8"),
        "memoryview": memoryview(bytes(json_data["memoryview"], "utf-8")),
        "none": json_data["none"],  # already None
        "range": range(len(json_data["range"]))  # reconstructs based on length
    }

    print("\nReconstructed Python Object:")
    for key, value in reconstructed.items():
        print(f"{key}: {value} | Type: {type(value)}")


# --- Run all conversions ---
json_string = convert_to_json_string()
convert_to_json_file()
convert_back_from_json()

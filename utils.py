import json


def to_dict(data: bytes) -> dict:
    # decode the bytes into a string
    data_string = data.decode("utf-8")

    # parse the string as JSON and convert it to a dictionary
    return json.loads(data_string)


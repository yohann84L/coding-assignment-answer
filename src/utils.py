import json


def int_size(integer):
    return len("%i" % integer)


def read_json(json_filepath):
    with open(json_filepath) as json_file:
        data = json.load(json_file)
        return data

from pprint import pprint
from flask import jsonify

values = {}

def add_value(value):
    if value in values:
        values[value] += 1
    else:
        values[value] = 1

    return jsonify({"value_times": values[value]})
import json
import sys

from pprint import pprint


def load_data(filepath):
    with open(filepath, "r") as file:
        return json.loads(file.read())


def pretty_print_json(data):
    pprint(data, indent=4)


if __name__ == "__main__":
    if sys.argv < 2:
        print("Usage: {0} <json_file>".format(sys.argv[0]))
        sys.exit(1)

    filepath = sys.args[1]

    try:
        data = load_data(filepath)
    except IOError as e:
        print("Open {0} error: {1}".format(filepath,e))
        sys.exit(1)

    try:
        pretty_print_json(data)
    except Exception as e:
        print("Pretty printing error: {0}".format(e))

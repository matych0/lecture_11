import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    return data[field]


def linear_search(sequential_data, number):
    keys = ["position", "count"]
    combined = []
    positions = []
    quantity = 0
    for pos, num in enumerate(sequential_data):
        if num == number:
            quantity = quantity + 1
            positions.append(pos)
    combined.append(positions)
    combined.append(quantity)
    count_pos_dict = dict(zip(keys, combined))
    return count_pos_dict


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    results = linear_search(sequential_data, 10)
    print(results)
if __name__ == '__main__':
    main()
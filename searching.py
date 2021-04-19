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


def pattern_search(sequence, pattern):
    pos = set()
    idx = 0
    while idx < len(sequence) - len(pattern):
        index = 0
        while index < len(pattern):
            if sequence[idx + index] == pattern[index]:
                index = index +1
            else:
                break
        else:
            pos.add(idx)
        idx = idx + 1
    return pos


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    results = linear_search(sequential_data, 10)
    print(results)

    sequential_data = read_data("sequential.json", "dna_sequence")
    my_pattern = "ATA"
    results = pattern_search(sequential_data, my_pattern)
    print(results)
if __name__ == '__main__':
    main()
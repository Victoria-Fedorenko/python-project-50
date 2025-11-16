import json
from pathlib import Path

import yaml


def read_files(file1, file2):

    def read_file(file_path_str):
        file_path = Path(file_path_str)
        file_extension = file_path.suffix
        if file_extension in ['.yml', '.yaml']:
            with open(file_path, 'r') as my_file:
                try:
                    my_data = yaml.safe_load(my_file)
                    return my_data
                except yaml.YAMLError as e:
                    print(f"Ошибка в YAML: {e}")
                    print("Содержимое файла:")
                    print(my_file.read())
        elif file_extension == '.json':
            with open(file_path, 'r') as my_file:
                try:
                    my_data = json.load(my_file)
                    return my_data
                except json.JSONDecodeError as e:
                    print(f"Ошибка в JSON: {e}")
                    print("Содержимое файла:")
                    print(my_file.read())    

    data_1 = read_file(file1)
    data_2 = read_file(file2)

    return data_1, data_2


def find_the_same_data(data_1, data_2):

    keys_1 = data_1.keys()
    keys_2 = data_2.keys()

    result = {}

    for k in keys_1:

        if k in keys_2:

            if data_1[k] == data_2[k]:

                val = data_1[k]

                result[k] = val

    return result


def find_removed_data(data_1, data_2):

    keys_1 = data_1.keys()
    keys_2 = data_2.keys()

    result = {}

    for k in keys_1:

        if k not in keys_2:

            val = data_1[k]

            result[k] = val
    
    return result


def find_added_data(data_1, data_2):

    keys_1 = data_1.keys()
    keys_2 = data_2.keys()

    result = {}

    for k in keys_2:

        if k not in keys_1:

            val = data_2[k]

            result[k] = val
    
    return result


def find_changed_data(data_1, data_2):

    keys_1 = data_1.keys()
    keys_2 = data_2.keys()

    before_change = {}
    after_change = {}

    for k in keys_1:

        if k in keys_2:

            if data_1[k] != data_2[k]:

                val1 = data_1[k]
                val2 = data_2[k]

                before_change[k] = val1
                after_change[k] = val2

    return before_change, after_change


def get_categorized_data(data_1, data_2):

    same_data = find_the_same_data(data_1, data_2)
    removed_data = find_removed_data(data_1, data_2)
    added_data = find_added_data(data_1, data_2)
    before_change, after_change = find_changed_data(data_1, data_2)

    return same_data, removed_data, added_data, before_change, after_change
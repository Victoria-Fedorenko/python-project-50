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
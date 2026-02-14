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


def get_tree_with_categories(before, after):
	accumulator = {}
	before_keys = set(before.keys())
	after_keys = set(after.keys())
	removed_keys = before_keys - after_keys
	added_keys = after_keys - before_keys

	common_keys = before_keys & after_keys
	for key in removed_keys:
		accumulator[key] = {
			"_value": before[key],
			"_status": "removed"
		}
	for key in added_keys:
		accumulator[key] = {
			"_value": after[key],
			"_status": "added"
		}
	for key in common_keys:
		if before[key] == after[key]:
			accumulator[key] = {
				"_value": before[key],
				"_status": "unchanged"
			}
		elif isinstance(before[key], dict) and isinstance(after[key], dict):
			accumulator[key] = {
				**get_tree_with_categories(before[key], after[key]),
				"_status": "recursive"
			}
		else:
			accumulator[key] = {
				"_value": before[key],
				"_new_value": after[key],
				"_status": "changed"
			}

	return accumulator


def get_nested_keys(d):
	items = []

	def actual_get_nested_keys(d, parent_key='', sep='.'):
		for k, v in d.items():
			if k not in ['_status', '_value', '_new_value']:
				new_key = parent_key + sep + str(k) if parent_key else str(k)
				items.append(new_key)
				if isinstance(v, dict):
					actual_get_nested_keys(v, new_key, sep=sep)
		return items
	return actual_get_nested_keys(d, parent_key='', sep='.')


def get_value_by_nested_key(d, full_key, sep='.'):
    keys = full_key.split(sep)
    current_value = d
    for key in keys:
        if isinstance(current_value, dict) and key in current_value:
            current_value = current_value[key]
        else:
            return None
    return current_value
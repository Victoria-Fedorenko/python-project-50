def get_nested_keys(d):
	items = []
	def actual_get_nested_keys(d, parent_key='', sep='.'):
		for k, v in d.items():
			if k not in ['_status', '_value', '_newValue']:
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
            return None # Или бросить KeyError
    return current_value


def plain_format_diff(my_tree):
	
    my_keys = sorted(get_nested_keys(my_tree))

    def format_value_from_node(node, v):
        value = node.get(v, '')
        if isinstance(value, dict):
            return '[complex value]'
        elif isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return 'null'
        elif isinstance(value, str):
            return f"'{value}'"
        return value

    result = ''
    for key in my_keys:
        node = get_value_by_nested_key(my_tree, key)
        if node is None:
            continue
        status = node.get('_status')
        if status == "removed":
            result += f"Property {key} was removed\n"
        elif status == "added":
            value = format_value_from_node(node, '_value')
            result += f"Property {key} was added with value: {value}\n"
        elif status == "changed":
            old_value = format_value_from_node(node, '_value')
            new_value = format_value_from_node(node, '_newValue')
            result += f"Property {key} was updated. From {old_value} to {new_value}\n"

    return result
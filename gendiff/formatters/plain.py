from gendiff.scripts.parse_data import get_nested_keys, get_value_by_nested_key


def plain_format_diff(my_tree):  # noqa: C901
	
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
            result += f"Property '{key}' was removed\n"
        elif status == "added":
            value = format_value_from_node(node, '_value')
            result += f"Property '{key}' was added with value: {value}\n"
        elif status == "changed":
            old_value = format_value_from_node(node, '_value')
            new_value = format_value_from_node(node, '_new_value')
            result += (
                f"Property '{key}' was updated. "
                f"From {old_value} to {new_value}\n"
            )

    return result.rstrip('\n')
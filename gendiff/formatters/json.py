from gendiff.scripts.parse_data import get_nested_keys, get_value_by_nested_key
import json

def json_format_diff(my_tree):

	def format_value_from_node(node, v):
		value = node.get(v, '')
		if isinstance(value, bool):
			return str(value).lower()
		elif value is None:
			return 'null'
		elif isinstance(value, str):
			return f"'{value}'"
		return value

	def format_json(my_tree):
		my_keys	= sorted(get_nested_keys(my_tree))
		result_removed = {}
		result_added = {}
		result_changed = {}
		for key in my_keys:
			node = get_value_by_nested_key(my_tree, key)
			if node is None:
				continue
			status = node.get('_status')
			if status == "removed":
				value = format_value_from_node(node, '_value')
				result_removed[key] = value
			elif status == "added":
				value = format_value_from_node(node, '_value')
				result_added[key] = format_value_from_node(node, '_value')
			elif status == "changed":
				old_value = format_value_from_node(node, '_value')
				new_value = format_value_from_node(node, '_new_value')
				result_changed[key] = [old_value, new_value]

			result_total = {
				"removed": result_removed,
				"added": result_added, 
				"updated": result_changed
				}

		return json.dumps(result_total, indent=2)
	
	return format_json(my_tree)
def stylish_format_diff(tree):  # noqa: C901
	def normalize(v):
		if isinstance(v, bool):
			return str(v).lower()
		if v is None:
			return 'null'
		return str(v)
	
	def actual_formatter(my_tree, current_depth=0):  # noqa: C901
		acc = ''
		key_indent = "    " * (current_depth + 1)
		marker_indent = "    " * current_depth + "  "

		def format_value(value):
			if isinstance(value, dict):
				inner = (
					'{\n' + actual_formatter(value, current_depth + 1)
					+ marker_indent + '  }'
				)
			else:
				inner = normalize(value)
			return f"{inner}\n"
		
		sorted_keys = sorted(my_tree.keys())

		for key in sorted_keys:
			node = my_tree[key]
			if not isinstance(node, dict):
				acc += f'{key_indent}{key}: {normalize(node)}\n'
				continue

			if '_status' not in node:
				acc += f'{key_indent}{key}: {format_value(node)}'
				continue

			status = node.get('_status')

			if status == "recursive":
				acc += f'{key_indent}{key}: {{\n'
				child = {kk: vv for kk, vv in node.items() if kk != '_status'}
				acc += actual_formatter(child, current_depth + 1)
				acc += f'{key_indent}}}\n'

			elif status == "removed":
				value = node.get('_value', '')
				acc += f'{marker_indent}- {key}: {format_value(value)}'

			elif status == "added":
				value = node.get('_value', '')
				acc += f'{marker_indent}+ {key}: {format_value(value)}'

			elif status == "changed":
				old_value = node.get('_value', '')
				new_value = node.get('_new_value', '')
				acc += f'{marker_indent}- {key}: {format_value(old_value)}'
				acc += f'{marker_indent}+ {key}: {format_value(new_value)}'

			elif status == "unchanged":
				value = node.get('_value', '')
				acc += f'{key_indent}{key}: {format_value(value)}'

		return acc

	return f'{{\n{actual_formatter(tree)}}}'
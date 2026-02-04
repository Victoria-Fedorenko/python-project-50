def stylish_format_diff(tree):
	def normalize(v):
		if isinstance(v, bool):
			return str(v).lower()
		if v is None:
			return 'null'
		return str(v)
	
	

	def actual_formatter(my_tree, current_depth=1):
		acc = ''
		indent = "    " * current_depth

		def format_value(value):
			if isinstance(value, dict):
				inner = '{\n' + actual_formatter(value, current_depth + 1) + indent + '  }'
			else:
				inner = normalize(value)
			return f"{inner}\n"
		
		sorted_keys = sorted(my_tree.keys())

		for key in sorted_keys:
			node = my_tree[key]
			if not isinstance(node, dict):
				acc += f'{indent}  {key}: {normalize(node)}\n'
				continue

			if '_status' not in node:
				acc += f'{indent}  {key}: {format_value(node)}'
				continue

			status = node.get('_status')

			if status == "recursive":
				acc += f'{indent}  {key}: {{\n'
				child = {kk: vv for kk, vv in node.items() if kk != '_status'}
				acc += actual_formatter(child, current_depth + 1)
				acc += f'{indent}}}\n'

			elif status == "removed":
				value = node.get('_value', '')
				acc += f'{indent}- {key}: {format_value(value)}'

			elif status == "added":
				value = node.get('_value', '')
				acc += f'{indent}+ {key}: {format_value(value)}'

			elif status == "changed":
				old_value = node.get('_value', '')
				new_value = node.get('_new_value', '')
				acc += f'{indent}- {key}: {format_value(old_value)}'
				acc += f'{indent}+ {key}: {format_value(new_value)}'

			elif status == "unchanged":
				value = node.get('_value', '')
				acc += f'{indent}  {key}:  {format_value(value)}'

		return acc

	return actual_formatter(tree)
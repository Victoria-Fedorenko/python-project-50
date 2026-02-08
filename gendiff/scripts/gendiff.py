
import argparse

from gendiff.formatters.json import json_format_diff
from gendiff.formatters.plain import plain_format_diff
from gendiff.formatters.stylish import stylish_format_diff
from gendiff.scripts.parse_data import read_files, get_tree_with_categories

FORMATTERS = {
    "stylish": stylish_format_diff,
     "plain": plain_format_diff,
     "json": json_format_diff,
}


def generate_diff(file1, file2, formatter=stylish_format_diff):

    data_1, data_2 = read_files(file1, file2)
    my_tree = get_tree_with_categories(
        data_1,
        data_2,
    )
    
    if isinstance(formatter, str):
        formatter = FORMATTERS.get(formatter, stylish_format_diff)

    result = formatter(my_tree)

    return result
    

def main():

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    
    parser.add_argument('first_file')

    parser.add_argument('second_file')

    parser.add_argument(
        '-f',
        '--format',
        choices=list(FORMATTERS.keys()),
        default='stylish',
        help='Output format (default: stylish)',
    )

    args = parser.parse_args()

    formatter = FORMATTERS.get(args.format, stylish_format_diff)
    result = generate_diff(
        args.first_file,
        args.second_file,
        formatter=formatter,
    )

    print(result)


if __name__ == '__main__':
    main()
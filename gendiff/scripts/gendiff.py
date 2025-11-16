
import argparse

# from gendiff.formatters.json import json_formatter
# from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.scripts.parse_data import get_categorized_data, read_files

FORMATTERS = {
    "stylish": stylish,
    # "plain": plain,
    # "json": json_formatter,
}


def generate_diff(file1, file2, formatter=stylish):

    data_1, data_2 = read_files(file1, file2)
    (
        same_data,
        removed_data,
        added_data,
        before_change,
        after_change,
    ) = get_categorized_data(
        data_1,
        data_2,
    )
    
    if isinstance(formatter, str):
        formatter = FORMATTERS.get(formatter, stylish)

    result = formatter(
        same_data,
        removed_data,
        added_data,
        before_change,
        after_change,
    )

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

    formatter = FORMATTERS.get(args.format, stylish)
    result = generate_diff(
        args.first_file,
        args.second_file,
        formatter=formatter,
    )

    print(result)


if __name__ == '__main__':
    main()
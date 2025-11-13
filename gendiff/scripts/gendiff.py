import argparse

def main():

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    
    parser.add_argument('first_file')

    parser.add_argument('second_file')

    # parser.add_argument(
    #     '-f',
    #     '--format',
    #     choices=list(FORMATTERS.keys()),
    #     default='stylish',
    #     help='Output format (default: stylish)',
    # )

    parser.parse_args()

    # formatter = FORMATTERS.get(args.format, stylish)
    # result = generate_diff(
    #     args.first_file,
    #     args.second_file,
    #     formatter=formatter,
    # )


if __name__ == '__main__':
    main()
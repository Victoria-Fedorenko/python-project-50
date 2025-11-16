from gendiff.scripts.gendiff import generate_diff
from gendiff.formatters.stylish import stylish
# from gendiff.formatters.plain import plain
# import json
# from gendiff.formatters.json import json_formatter


def load_expected(name):

    path = f'tests/expected/{name}'
    with open(path, 'r') as fh:
        return fh.read()


def test_generate_diff():
    expected_stylish_short = load_expected('stylish_short.txt')
    # expected_plain = load_expected('plain.txt')
    # expected_json = json.loads(load_expected('json.json'))

    assert generate_diff('tests/test_data/file1.json', 
                         'tests/test_data/file2.json') == expected_stylish_short
    assert generate_diff('tests/test_data/file1.json', 
                         'tests/test_data/file2.json', 
                         stylish) == expected_stylish_short
    assert generate_diff('tests/test_data/filepath1.yml', 
                         'tests/test_data/filepath2.yml') == expected_stylish_short
    # assert generate_diff('tests/test_data/file1.json', 
    #                      'tests/test_data/file2.json', 
    #                      plain) == expected_plain
    # assert json.loads(generate_diff(
    #                     'tests/test_data/file1.json', 
    #                      'tests/test_data/file2.json', 
    #                      json_formatter)) == expected_json
    
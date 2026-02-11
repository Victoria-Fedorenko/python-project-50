from gendiff.scripts.gendiff import generate_diff
from gendiff.formatters.stylish import stylish_format_diff
from gendiff.formatters.plain import plain_format_diff
import json
from gendiff.formatters.json import json_format_diff


def load_expected(name):

    path = f'tests/expected/{name}'
    with open(path, 'r') as fh:
        return fh.read()


def test_generate_diff():
    expected_stylish_short = load_expected('stylish_short.txt')
    expected_stylish_long = load_expected('stylish_long.txt')
    expected_plain = load_expected('plain.txt')
    expected_json = json.loads(load_expected('json.json'))

    assert generate_diff('tests/test_data/long1.json', 
                         'tests/test_data/long2.json') == expected_stylish_long
    assert generate_diff('tests/test_data/long1.json', 
                         'tests/test_data/long2.json', 
                         stylish_format_diff) == expected_stylish_long
    assert generate_diff('tests/test_data/long1.json', 
                         'tests/test_data/long2.json', 
                         plain_format_diff) == expected_plain
    assert json.loads(generate_diff(
                        'tests/test_data/long1.json', 
                         'tests/test_data/long2.json', 
                         json_format_diff)) == expected_json
    assert (generate_diff('tests/test_data/filepath1.yml', 
                         'tests/test_data/filepath2.yml', 
                         stylish_format_diff)) == expected_stylish_long
    
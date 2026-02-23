#Difference Calculator

##Tests and linter status
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Victoria-Fedorenko_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Victoria-Fedorenko_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Victoria-Fedorenko_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Victoria-Fedorenko_python-project-50)
[![Actions Status](https://github.com/Victoria-Fedorenko/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Victoria-Fedorenko/python-project-50/actions)

##General info

This CLI tool can help you to compare two configuration files using gendiff function.
You can compare json-files and yml-files.

To install the package clone the repository and enter the project folder.
After that you can build the project with
```bash
uv build
```

You can use this tool with or without format option. 
Format options available: stylish, plain, json. Watch demonstration to see the difference. 

EXAMPLE:

```bash
gendiff file1.json file2.json
# or with format option
gendiff -f json file1.yml file2.yml
```
#!/usr/bin/python3
import json
import sys

tests_file = sys.argv[1]  # 'tasksNT/tests.json'
values_file = sys.argv[2]  # 'tasksNT/values.json'

with open(tests_file, 'r') as tests_file:
    tests = json.load(tests_file)

with open(values_file, 'r') as values_file:
    values = json.load(values_file)


def rec(js):
    for elem in js:
        if 'id' in elem:
            if 'value' in elem:
                for value in values['values']:
                    if elem['id'] == value['id']:
                        elem['value'] = value['value']

            if 'values' in elem:
                rec(elem["values"])


rec(tests['tests'])

file_report = 'report.json'

with open(file_report, 'w') as write_file:
    json.dump(tests, write_file, indent=2)

print(f'file {file_report} was created')

from collections import defaultdict
import csv


def nested_dict(n, element_type):
    if n == 1:
        return defaultdict(element_type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, element_type))

MAPPINGS_FILE = 'mapping.csv'

mapping = nested_dict(2, str)

with open(MAPPINGS_FILE, 'r') as csv_input:
    spamreader = csv.reader(csv_input, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='`')
    for row in spamreader:
        print(row)
        # if len(row) > 0:
        #     file_name, key, ignore, *mapped_key = row
        #     print(file_name, key)
        #     if mapped_key:
        #         mapping[file_name][key] = mapped_key


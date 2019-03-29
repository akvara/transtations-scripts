from collections import defaultdict
import csv


def nested_dict(n, element_type):
    if n == 1:
        return defaultdict(element_type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, element_type))


translations = nested_dict(2, str)
translations_file = 'translations.csv'
with open(translations_file, 'r') as csv_input:
    spamreader = csv.reader(csv_input, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='|')
    for row in spamreader:
        if len(row) > 0:
            print(row)

            language, key, translation = row
            translations[language][key] = translation

# mapping = nested_dict(3, str)
# mapping_file = 'mapping.csv'
#
# with open(mapping_file, 'r') as csv_input:
#     spamreader = csv.reader(csv_input, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='|')
#     for row in spamreader:
#         if len(row) > 0:
#             file_name, key, translated_key = row
#             mapping[file_name][key]['aha'] = translated_key

# print(translations['locale-de']['VARIABLE.SENSOR_RDNG'])
if translations['locale-de']['VARIABLE.k']:
    print(translations['locale-de']['VARIABLE.SENSOR_RDNG'])
# print(mapping[file_name][key]['aha'])

import csv
import json
import os
import sys

EXCEPT_FILES = ['importer_errors.json']
ONLY_FILE = 'importer.json'


def decompose(array, path, input):
    if type(input).__name__ == 'str':
        array.append((path, input))
    else:
        for key in input:
            decompose(array, path + "." + key if path else key, input[key])


if __name__ == '__main__':
    if not len(sys.argv) == 3:
        sys.stdout.write("Usage: {} locales_directory output_file\n".format(sys.argv[0]))
        sys.exit(-1)
    locales_directory = sys.argv[1]
    output_file = sys.argv[2]

    files = []
    count_files = 0
    count_lines = 0

    for file in os.listdir(locales_directory):
        if '.json' in file and file not in EXCEPT_FILES:
            files.append(file)

    # files = [ONLY_FILE]

    with open(output_file, 'w') as csv_output:
        spam_writer = csv.writer(csv_output, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='`')
        for file in files:
            count_files += 1
            with open(os.path.join(locales_directory, file)) as json_data:
                en_translations = json.load(json_data)
                result = []
                decompose(result, None, en_translations)
                for (key, value) in result:
                    count_lines += 1
                    spam_writer.writerow([os.path.splitext(file)[0], key, value])

    print(f"\nResult ({count_files} files, {count_lines} lines) written to '{output_file}'\n")

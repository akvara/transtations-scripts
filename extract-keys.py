import csv
import json
import os
import sys

OUTPUT_FILE_NAME = 'mapping.csv'
EXCEPT_FILES = ['importer.json', 'auth.json']

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        sys.stdout.write("Usage: {} locales_directory\n".format(sys.argv[0]))
        sys.exit(-1)
    locales_directory = sys.argv[1]

    files = []
    count_files = 0
    count_lines = 0

    # r=root, d=directories, f = files
    for r, d, f in os.walk(os.path.join(locales_directory, 'en')):
        for file in f:
            if '.json' in file and file not in EXCEPT_FILES:
                files.append(file)

    with open(OUTPUT_FILE_NAME, 'w') as csv_output:
        spam_writer = csv.writer(csv_output, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        for file in files:
            count_files += 1
            with open(os.path.join(locales_directory, 'en', file)) as json_data:
                en_translations = json.load(json_data)
                for key in en_translations:
                    count_lines += 1
                    if type(en_translations[key]).__name__ != 'str':
                        print("File " + file + " key " + key + " has incorrect type (" + type(
                            en_translations[key]).__name__ + ") of value: ", en_translations[key])
                    else:
                        spam_writer.writerow([os.path.splitext(file)[0], key, '"' + en_translations[key] + '"'])

    print(f"\nResult ({count_files} files, {count_lines} lines) written to '{OUTPUT_FILE_NAME}'\n")

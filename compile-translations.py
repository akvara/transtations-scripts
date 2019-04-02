import os
import json
import sys

from collections import defaultdict
import csv

LANGUAGES = [
    'en'
    # 'da', 'de', 'en', 'es', 'fr', 'it', 'ja', 'nl', 'pt', 'ru',
]

OUTPUT_DIRECTORY = 'locales'
TRANSLATIONS_FILE = 'translations.csv'
MAPPINGS_FILE = 'mapping.csv'
EXCEPT_FILES = ['importer_errors.json']


def nested_dict(n, element_type):
    if n == 1:
        return defaultdict(element_type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, element_type))


if __name__ == '__main__':
    if not len(sys.argv) == 2:
        sys.stdout.write("Usage: {} locales_directory\n".format(sys.argv[0]))
        sys.exit(-1)
    locales_directory = sys.argv[1]

    files = []
    missing_translations = 0

    '''
    Read in translations
    '''
    translations = nested_dict(2, str)
    with open(TRANSLATIONS_FILE, 'r') as csv_input:
        spam_reader = csv.reader(csv_input, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='`')
        for row in spam_reader:
            if len(row) > 0:
                try:
                    language, key, translation = row
                    translations[language][key] = translation
                except:
                    print("Problem in data row:", row)

    '''
    Read in mappings
    '''
    mapping = nested_dict(2, str)

    with open(MAPPINGS_FILE, 'r') as csv_input:
        spam_reader = csv.reader(csv_input, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='`')
        for row in spam_reader:
            if len(row) > 0:
                try:
                    file_name, key, ignore, mapped_key, *comment = row
                    if mapped_key:
                        mapping[file_name][key] = mapped_key
                except:
                    print("Problem in data row:", row)

    '''
    Read files in directory
    '''
    # r=root, d=directories, f = files
    for r, d, f in os.walk(os.path.join(locales_directory, 'en')):
        for file in f:
            if '.json' in file and not file in EXCEPT_FILES:
                files.append(file)

    # files = ['growers.json']
    for file in files:
        file_name = os.path.splitext(file)[0]
        # print("Reading file " + file)
        with open(os.path.join(locales_directory, 'en', file)) as json_data:
            en_translations = json.load(json_data)

        for lang in LANGUAGES:
            directory = os.path.join(locales_directory, lang)
            # Create directory, if does not exist
            if not os.path.exists(directory):
                # print("Creating directory " + directory)
                os.makedirs(directory)

            translation_file_name = os.path.join(directory, file)

            with open(translation_file_name, 'w', encoding='utf8') as outfile:
                file_content = dict()
                # print("Exporting to file file " + translation_file_name)
                for key in en_translations:
                    mapped_key = mapping[file_name][key]
                    if mapped_key:
                        translated_string = translations[f'locale-{lang}'][mapped_key]
                        file_content[key] = translated_string
                    else:
                        print(f'No translation key for {file_name}:{key}')
                        missing_translations += 1
                json.dump(file_content, outfile, indent=2, ensure_ascii=False)
    print(f"Done. {missing_translations} missing translations")

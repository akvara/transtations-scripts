import os
import json
import sys
import settings

OUTPUT_DIRECTORY = 'locales'

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        sys.stdout.write("Usage: {} locales_directory\n".format(sys.argv[0]))
        sys.exit(-1)
    locales_directory = sys.argv[1]

    files = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(os.path.join(locales_directory, 'en')):
        for file in f:
            if '.json' in file:
                files.append(file)

    # Example
    # data = dict()
    # data['people'] = []
    # data['people'].append({
    #     'name': 'Scott',
    #     'website': 'stackabuse.com',
    #     'from': 'Nebraska'
    # })

    # temp
    files = ['legend.json']
    for file in files:
        print("Reading file " + file)
        with open(os.path.join(locales_directory, 'en', file)) as json_data:
            en_translations = json.load(json_data)
            # for key in en_translations:
            #     print(key, en_translations[key])
            # print(en_translations)

        for lang in settings.LANGUAGES:
            directory = os.path.join(OUTPUT_DIRECTORY, lang)
            # Create directory, if does not exist
            if not os.path.exists(directory):
                print("Creating directory " + directory)
                os.makedirs(directory)

            translation_file_name = os.path.join(directory, file)
            with open(translation_file_name, 'w') as outfile:
                print("Exporting to file file " + translation_file_name)
                json.dump(en_translations, outfile)

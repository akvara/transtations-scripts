Python >=3.6 is required

- `extract-keys.py` extracts keys of all files in given directory to specified output file as CSV

#### 1. Get keys from locale/en files:
```bash
python3 extract-keys.py {path-to-src/locales/en} mapping.csv
```
#### 2. Fill mapping.csv with 'translation-key'
```text
'file','key','ignore','translation-key'
```

#### 4. Get keys from translation files directory to translations.csv (append -delta directory files, if needed):
```bash
python3 extract-keys.py {path-to-src/mentor-locale} translations.csv
```
#### 4. Make sure all required LANGUAGES are listed in settings.py

#### 5. Make compilations:
```bash
python3 compile-translations.py {path-to-src/locales}
```
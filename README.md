Python >=3.6 is required

### 1. Get keys from locale files:
```bash
python3 extract-keys.py {path-to-src/locales}
```
### 2. Rename initial-mapping.csv to mapping.csv and fill data

### 3. Make sure all required LANGUAGES are listed in settings.py

### 4. Make compilations:
```bash
python3 compile-translations.py {path-to-src/locales}
```
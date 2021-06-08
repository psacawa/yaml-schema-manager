### yaml-schema-manager

```
usage: schema.py [-h] [--dry-run] [-c] pattern

Prosty skrypt który ściąga schematy JSON z katalogu JSON SchemaStore których
nazy pasują do wzorca i drukujęwzorce glob na pole 'yaml.schemas' w yaml-
language-server

positional arguments:
  pattern     Wyrażenie regularne dopasowane to nazw schematów

optional arguments:
  -h, --help  show this help message and exit
  --dry-run   Nie ściągaj schematów, tylko wypisz 'yaml.schemas'
  -c, --clip  skopiuj 'yaml.schemas' do klipsu
```

#!/usr/bin/env python3

import argparse
import json
import os
import re
import sys
from pprint import pprint

import jq
import requests
import pyperclip


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("-c", "--clip", action="store_true")
    args = parser.parse_args(sys.argv[1:])
    pattern = args.pattern
    catalog = json.load(open("./catalog.json", "r"))
    schemas = (
        jq.compile(f'.schemas[]|select(.name|test("{pattern}"))').input(catalog).all()
    )
    schema_config = {}
    for schema in schemas:
        print(f"Fetching {schema['name']} from {schema['url']}")
        filename = schema_filename(schema["name"])
        if 'fileMatch' in schema:
            schema_config[f"file://{os.getcwd()}/{filename}"] = schema["fileMatch"]
        if not args.dry_run:
            req = requests.get(schema["url"])
            if req.status_code == 200:
                with open(filename, "wb") as file:
                    file.write(req.content)
            else:
                print(f"Request failed: {req.status_code}", file=sys.stderr)
    config_output = json.dumps(schema_config)
    if args.clip:
        pyperclip.copy(config_output)
    else:
        pprint(json.dumps(schema_config))


def schema_filename(name):
    sanitized_name = re.sub(r"(^\.)|[^-\w\d\.]", "", name)
    return f"{sanitized_name}.schema.json"


if __name__ == "__main__":
    main()

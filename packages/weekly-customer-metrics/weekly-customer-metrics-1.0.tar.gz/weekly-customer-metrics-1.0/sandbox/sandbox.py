import json

import awswrangler as wr
from smart_open import smart_open


def read_json_file_into_dict(file_path):
    with smart_open(file_path, 'rb') as stream:
        data = json.load(stream)
        return data

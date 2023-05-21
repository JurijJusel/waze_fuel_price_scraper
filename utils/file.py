from pathlib import Path
import json


def create_json(data, json_file):
    path = Path(f"data/{json_file}")
    if path.is_file():
        with open(path, "a") as file:
            json.dump(data, file, indent=2)
            return f'The data is added to the <{json_file}> file'
    else:
        with open(path, "w") as file:
            json.dump(data, file, indent=2)
            return f'created <{json_file}> file and data written to it'
        

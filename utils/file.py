from pathlib import Path
import json


def create_json(data, json_file):
    path = Path(f"data/{json_file}")
    if path.is_file():
        with open(path, "a") as file:
            if data:  # Check if data list is not empty
                json.dump(data, file, indent=2)
                file.write('\n')
                return f'The data is added to the file <{json_file}>'
            else:
                return f'The data list is empty. Nothing was written to file <{json_file}>'
    else:
        with open(path, "w") as file:
            if data:  # Check if data list is not empty
                json.dump(data, file, indent=2)
                file.write('\n')
                return f'Created <{json_file}> file and data written to it'
            else:
                return f'Created <{json_file}> file, data list is empty!!!'
                  
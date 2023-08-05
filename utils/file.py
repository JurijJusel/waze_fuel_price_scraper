from pathlib import Path
import json


def create_json(new_data, json_file):
    path = Path(f"data/{json_file}")
    if path.is_file():
        with open(path, "r+") as file:
            try:
                json_obj = json.load(file)
            except json.JSONDecodeError:
                json_obj = []
            combined_data = json_obj + new_data

        with open(path, "w") as file:
            if combined_data:
                json.dump(combined_data, file, indent=2)
                return f'The data is added to the file <{json_file}>'
            else:
                return f'The data list is empty. Nothing was written to file <{json_file}>'
    else:
        with open(path, "w") as file:
            if new_data: 
                json.dump(new_data, file, indent=2)
                return f'Created <{json_file}> file and data written to it'
            else:
                return f'Created <{json_file}> file, data list is empty!!!'
    
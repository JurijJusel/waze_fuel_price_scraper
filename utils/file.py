from pathlib import Path
import json


def create_json(new_data, json_file_path):
    path = Path(f"{json_file_path}")
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
                return f'The data is added to the file <{json_file_path}>'
            else:
                return f'The data list is empty. Nothing was written to file <{json_file_path}>'
    else:
        with open(path, "w") as file:
            if new_data: 
                json.dump(new_data, file, indent=2)
                return f'Created <{json_file_path}> file and data written to it'
            else:
                return f'Created <{json_file_path}> file, data list is empty!!!'


def read_json(json_file_path):  # open json file if file is empty, output file with []
    path = Path(f"{json_file_path}")
    try:
        with open(path, 'r') as file:
            data = file.read()
            if data:
                return json.loads(data)
            else:
                return []
    except FileNotFoundError:
        print(f"File '{json_file_path}' not found. Creating a new file.")
        with open(path, 'w') as new_file:
            new_file.write("[]")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{json_file_path}'.")
        return []
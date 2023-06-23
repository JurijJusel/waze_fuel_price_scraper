from pathlib import Path
import json


def create_json(data, json_file):
    path = Path(f"data/{json_file}")
    if path.is_file():
        with open(path, "a") as file:
            if data:  # Check if data list is not empty
                json.dump(data, file, indent=2)
                file.write('\n')
                return f'The data is added to the <{json_file}> file'
            else:
                return f'The data list is empty. Nothing was written to <{json_file}> file.'
    else:
        with open(path, "w") as file:
            if data:  # Check if data list is not empty
                json.dump(data, file, indent=2)
                file.write('\n')
                return f'Created <{json_file}> file and data written to it'
            else:
                return f'Created <{json_file}> file, but the data list is empty.'


def write_to_txt_file(text, txt_file):
    try:
        with open(txt_file, 'a') as file:
            file.write(text + "\n")
        print(f"Successfully wrote the string to <{txt_file}>.")
    except IOError:
        print(f"Error: Failed not write to <{txt_file}>.")

        
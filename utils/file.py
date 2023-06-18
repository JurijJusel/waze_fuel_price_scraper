from pathlib import Path
import json


def create_json(data, json_file):
    path = Path(f"data/{json_file}")
    if path.is_file():
        with open(path, "a") as file:
            json.dump(data, file, indent=2)
            file.write('\n')
            return f'The data is added to the <{json_file}> file'
    else:
        with open(path, "w") as file:
            json.dump(data, file, indent=2)
            file.write('\n')
            return f'created <{json_file}> file and data written to it'


def write_to_txt_file(text, txt_file):
    try:
        with open(txt_file, 'a') as file:
            file.write(text + "\n")
        print(f"Successfully wrote the string to <{txt_file}>.")
    except IOError:
        print(f"Error: Failed not write to <{txt_file}>.")

        
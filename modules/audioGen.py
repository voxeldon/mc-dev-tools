import os
import json

def index_sound_files(directory, user_id):
    sound_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".wav") or file.endswith(".mp3") or file.endswith(".ogg"):
                sound_files.append(os.path.join(root, file))
    sound_definitions = {}
    for sound_file in sound_files:
        folder = os.path.dirname(os.path.relpath(sound_file, directory))
        file_name = os.path.basename(sound_file)
        if folder:
            sound_id = f"{user_id}.{folder.replace('/', '_')}"
        else:
            sound_id = f"{user_id}.{file_name.split('.')[0]}"
        sound_path = os.path.relpath(sound_file, directory).replace("\\", "/")
        sound_path = os.path.splitext(sound_path)[0]
        if sound_id in sound_definitions:
            sound_definitions[sound_id]["sounds"].append(f"sounds/{sound_path}")
        else:
            sound_definitions[sound_id] = {
                "category": "neutral",
                "sounds": [f"sounds/{sound_path}"]
            }
    data = {
        "format_version": "1.14.0",
        "sound_definitions": sound_definitions
    }
    with open("sound_definitions.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

user_id = input("Enter an identification name: ")
directory = "."
index_sound_files(directory, user_id)

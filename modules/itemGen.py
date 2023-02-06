import os
import json

def generate_lang_file(id, item_names):
    if os.path.exists("en_US.lang"):
        with open("en_US.lang", "r") as f:
            data = f.read()
        with open("en_US.lang", "a") as f:
            for item_name in item_names:
                if f"item.{id}:{item_name}.name" not in data:
                    f.write(f"item.{id}:{item_name}.name= {item_name.capitalize()}\n")
    else:
        with open("en_US.lang", "w") as f:
            for item_name in item_names:
                f.write(f"item.{id}:{item_name}.name= {item_name.capitalize()}\n")


def generate_json_files(id, item_names):
    for item_name in item_names:
        # BP JSON
        json1 = {
            "format_version": "1.10",
            "minecraft:item": {
                "description": {
                    "identifier": f"{id}:{item_name}"
                },
                "components": {
                    "minecraft:stacked_by_data": True,
                    "minecraft:hand_equipped": True,
                    "minecraft:max_stack_size": 64
                }
            }
        }

        with open(f"{item_name}.bp.json", "w") as f:
            json.dump(json1, f, indent=4)

        # RP JSON
        json2 = {
            "format_version": "1.10",
            "minecraft:item": {
                "description": {
                    "identifier": f"{id}:{item_name}",
                    "category": "Equipment"
                },
                "components": {
                    "minecraft:icon": f"{id}:{item_name}",
                    "minecraft:render_offsets": "miscellaneous",
                    "minecraft:hover_text_color": "white"
                }
            }
        }

        with open(f"{item_name}.rp.json", "w") as f:
            json.dump(json2, f, indent=4)

        # Item Texture JSON
        if os.path.exists("item_texture.json"):
            with open("item_texture.json", "r") as f:
                data = json.load(f)
                data["texture_data"][f"{id}:{item_name}"] = {
                    "textures": f"textures/items/{item_name}"
                }
            with open("item_texture.json", "w") as f:
                json.dump(data, f, indent=4)
        else:
            json3 = {
                "resource_pack_name": id,
                "texture_name": "atlas.items",
                "texture_data": {
                    f"{id}:{item_name}": {
                        "textures": f"textures/items/{item_name}"
                    }
                }
            }
            with open("item_texture.json", "w") as f:
                json.dump(json3, f, indent=4)

while True:
    id_input = input("Enter the id (e.g. loadisk): ")
    items_input = input("Enter the item names separated by a space (e.g. apple orange banana): ").split()
    generate_json_files(id_input, items_input)
    generate_lang_file(id_input, items_input)
    repeat = input("Generate more files? [y/n]: ")
    if repeat.lower() != "y":
        break

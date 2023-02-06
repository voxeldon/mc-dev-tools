import json

def generate_json():
    id = input("Enter id: ")
    board = input("Enter board: ")
    selector = input("Enter selector: ")

    new_data = {
        "translate": f"{id}.{board}",
        "with": {
            "rawtext": [
                {
                    "selector": selector
                },
                {
                    "score": {
                        "name": "selector",
                        "objective": board
                    }
                }
            ]
        }
    }

    try:
        with open("actionbar.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"rawtext": []}

    data["rawtext"].append(new_data)

    with open("actionbar.json", "w") as file:
        json.dump(data, file, separators=(",", ":"))

    print("Data added to the file successfully")

if __name__ == "__main__":
    while True:
        generate_json()

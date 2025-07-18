import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

def print_animal_info(animals):
    for animal in animals:
        if "name" in animal:
            print(f"Name: {animal['name']}")
        if "diet" in animal:
            print(f"Diet: {animal['diet']}")
        if "locations" in animal and animal["locations"]:
            print(f"Location: {animal['locations'][0]}")
        if "type" in animal:
            print(f"Type: {animal['type']}")
        print()  # blank line between animals

# Load and print the data
animals_data = load_data('animals_data.json')
print_animal_info(animals_data)


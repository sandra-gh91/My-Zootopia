import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
   return json.load(handle)


def get_animal_characteristic(animals_data):
    """ Returns the charactaristic of the animal """
    for animal in animals_data:
        print("Name:" ,animal['name'])
        print("Location:" ,animal['locations'][0])
        print("Diet:" ,animal['characteristics']["diet"])
        print("Type:" ,animal['characteristics']['type'])
        print("-" * 50)

animals_data = load_data('animals_data.json')
get_animal_characteristic(animals_data)




import json
import html
import tempfile


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
   return json.load(handle)

def generate_animals_html(animals_data):
    animals_html = ""
    for animal in animals_data:
        name = animal["name"]
        location = ",".join(animal["locations"])
        diet = animal["characteristics"].get("diet","N/A")
        a_type = animal["characteristics"].get("type","N/A")
        animals_html += f"""
        <li class="cards__item">
            <h2 class="card__title">{name}</h2>
            <p class="card__text">
                <strong>Location:</strong> {location}<br>
                <strong>Diet:</strong> {diet}<br>
                <strong>Type:</strong> {a_type}
            </p>
        </li>
        """
    return animals_html


def get_animal_characteristic(animals_data):
    """ Returns the charactaristic of the animal """
    for animal in animals_data:
        name = animal.get('name', 'N/A')
        location = animal['locations'][0] if animal.get('locations') else 'N/A'
        diet = animal['characteristics'].get('diet', 'N/A')
        a_type = animal['characteristics'].get('type', 'N/A')

        print("Name:", name)
        print("Location:", location)
        print("Diet:", diet)
        print("Type:", a_type)
        print("-" * 50)


def read_template(file_path):
    """Read the HTML template"""
    with open(file_path, "r") as file:
        return file.read()

def write_html(file_path, content):
    """Write HTML content to a file"""
    with open(file_path, "w") as file:
        file.write(content)

def main():

    animals_data = load_data("animals_data.json")
    get_animal_characteristic(animals_data)
    animals_html = generate_animals_html(animals_data)
    template_str = read_template("animals_template.html")
    final_html = template_str.replace("__REPLACE_ANIMALS_INFO__", animals_html)
    write_html("animals.html", final_html)
    print("HTML file 'animals.html` created successfully.")



if __name__ == "__main__":
    main()





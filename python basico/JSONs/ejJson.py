'''
Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de Manejo de JSON.
   Debe leer el archivo para importar los Pokémones existentes.
   Luego debe pedir la información del Pokémon a agregar.
   Finalmente debe guardar el nuevo Pokémon en el archivo.
'''

def read_JSON_file(file_path):
    import json
    with open(file_path, 'r') as file:
        data = json.load(file)
        print(f"File {file_path} read successfully!")
    return data


def write_JSON_file(file_path, data):
      import json
      with open(file_path, 'w') as file:
         json.dump(data, file, indent=4)
         print(f"File {file_path} written successfully!")


def add_new_pokemon(file_path):
   name = input("Name: ")
   type_ = input("Type: ")
   level = int(input("Level: "))
   weight_kg = float(input("Weight (kg): "))
   
   #turn a yes or no into a boolean value
   is_shiny = input("Is shiny? (yes/no)(y/n): ")
   if is_shiny.lower() == "yes" or is_shiny.lower() == "y":
      is_shiny = True
   else:
      is_shiny = False
   held_item = input("Held item: ")

   #string of skills
   skills_str = input("Skills (comma-separated): ")

   #list of skills
   skills = []
   for skill in skills_str.split(","):
      skills.append(skill.strip())

   # Stats
   stats = {
      "hp": int(input("HP: ")),
      "attack": int(input("Attack: ")),
      "defense": int(input("Defense: ")),
      "sp_attack": int(input("Sp. Attack: ")),
      "sp_defense": int(input("Sp. Defense: ")),
      "speed": int(input("Speed: ")),
   }

   pokemon = {
      "name": name,
      "type": type_,
      "level": level,
      "weight_kg": weight_kg,
      "is_shiny": is_shiny,
      "held_item": held_item,
      "skills": skills,
      "stats": stats,
   }

   return pokemon


def main():
   file_path = input("Enter the path to the Pokémon JSON file path: ")
   data = read_JSON_file(file_path)
   new_pokemon = add_new_pokemon(file_path)
   data.append(new_pokemon)
   write_JSON_file(file_path, data)
   print(f"New Pokémon {new_pokemon['name']} added successfully!")


if __name__ == "__main__":
   print("Welcome to the Pokémon JSON Manager!")
   main()

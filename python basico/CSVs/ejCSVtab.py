import csv


def write_vg_to_csv(file_path, data):  #name, genre, developer, rating
    with open(file_path, 'w', encoding = 'utf-8', newline='') as file:
        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames = headers, delimiter = "\t")  # delimiter defines which character we want to use to separate the vclues in the csv file
                                                                               # we can use: "," ";" "    "(tab) "|" "^" "~"
        writer.writeheader()

        writer.writerows(data)


def game_input(n):
    game_dict_list = []
    
    for i in range(n):
        print(f"Game {i + 1}: ")
        name = input("Name of the game: ")
        genre = input("Genre of the game: ")
        developer = input("Developer of the game: ")
        rating = input("Rating of the game: ")

        game_dict = {
            "name":name,
            "genre":genre,
            "developer":developer,
            "rating":rating
            }

        game_dict_list.append(game_dict)

    return game_dict_list

def main():
    n = int(input("How many games do you want to add to the list? "))
    games = game_input(n)
    file_name = input("File path and name: ")
    write_vg_to_csv(file_name, games)


if __name__ == "__main__":
    print("--- Listador de videojuegos ---")
    main()
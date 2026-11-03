'''
Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
'''


def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
    return lines


def sort_lines(lines):
    return sorted(lines)


def write_lines_to_file(path, lines):
    with open(path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')


def main(path):
    songs_path = path 
    sorted_songs_path = "sorted_songs.txt"                           #name of the file where the sorted songs will be saved
 
    songs_lines = read_file_by_lines(songs_path)                     #reads the songs from the file, line by line

    sorted_songs_lines = sort_lines(songs_lines)                     #sorts the songs alphabetically

    write_lines_to_file(sorted_songs_path, sorted_songs_lines)       #writes the sorted songs to a new file(creates the file)


if __name__ == "__main__":
    main("archivos/songs.txt")            #put the path of the file with the songs you want to sort
    print("The songs have been sorted and saved in 'sorted_songs.txt'.")

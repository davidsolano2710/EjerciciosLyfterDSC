'''
Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
    Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
'''

def string_word_sorter(string):

    words_list = []
    word = ""

    #this "for" separates the words in the string and puts them in a list
    for char in string:           
        if char != "-":
            word += char
        else:
            words_list.append(word)
            word = ""

    words_list.append(word)  # Add the last word to the list

    sorted_words_list = sorted(words_list)  # Sort the list of words alphabetically, I was going to do it manually, but sorted() is easier

    sorted_string = ""

    #this "for" converts the list back to a string with "-"
    for word in sorted_words_list:
        sorted_string += word + "-"

    sorted_string = sorted_string[:-1]  # Remove the last "-" from the string
    

    return sorted_string

print(string_word_sorter("python-variable-funcion-computadora-monitor-alacran"))

    
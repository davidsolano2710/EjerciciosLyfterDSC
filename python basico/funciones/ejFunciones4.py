'''
Cree una función que le dé la vuelta a un string y lo retorne.
    1.Esto ya lo hicimos en iterables.
    2.“Hola mundo” → “odnum aloH”
'''

def string_flip(string):
    flipped_string = ""

    for num in range(len(string)-1, -1, -1):
        flipped_string = flipped_string + string[num] 

    return flipped_string


print(string_flip("!dlrow olleh"))
print(string_flip("Hola mundo"))
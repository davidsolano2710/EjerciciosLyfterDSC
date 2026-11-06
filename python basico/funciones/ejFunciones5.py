'''
Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
    1.“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
'''

def lower_upper_counter(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upper_count += 1
        elif char in "abcdefghijklmnopqrstuvwxyz":
            lower_count += 1
    print(f"There’s {upper_count} upper cases and {lower_count} lower cases")
    return

lower_upper_counter("I love Nación Sushi")         # it doesn't count the accented letters, because they are not in the strings 
                                                   # used to check for upper and lower case letters.
                                                   # because of this, we could only use this function for any string in English, but not other
                                                   # languages that use accents

#I investigated and we can use isupper() and islower() to check instead of using a string

def lower_upper_counter2(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print(f"There’s {upper_count} upper cases and {lower_count} lower cases")
    return

lower_upper_counter2("I love Nación Sushi")        #this one counts the accented letters as well

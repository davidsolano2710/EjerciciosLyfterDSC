'''
Cree una función que retorne la suma de todos los números de una lista.
    1.La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
    2.[4, 6, 2, 29] → 41'''


def add_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


my_list = [1,2,3,4,5,6,7,8,9,10] # should return 55
my_list2 = [41,51,62,31,17,82,82] # 366

print(add_list(my_list))
print(add_list(my_list2))
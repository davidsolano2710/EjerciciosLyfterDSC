#Elimine impares de una lista
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []
for counter in range(0, len(my_list)):
    if my_list[counter] % 2 == 0:
        even_numbers.append(my_list[counter])


print(even_numbers)

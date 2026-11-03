#intercambiar el primer y ultimo elemento de una lista

my_list = [4, 3, 6, 1, 7]

first_element = my_list[0]                       #guardar el primer elemento

my_list[0] = my_list[-1]                         #ultimo se guarda en el primer espacio

my_list[-1] = first_element                      #elemento guardado(primero) se guarda en el ultimo espacio

print(my_list)                                   #prueba de que se intercambiaron




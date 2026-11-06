#imprimir un string letra por letra al reves

my_string = "Pizza con piña"

for counter in range(len(my_string)-1, -1, -1):  #(start, stop, step)
    print(my_string[counter])

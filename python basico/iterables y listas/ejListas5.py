#pedir al usuario 10 nums y alfinal mostrarlos y mostrar el mas alto
print("--- Ingrese 10 numeros y al final se le mostrara el mas alto. ---")

my_list = []

for n in range(10):
    num = int(input("Ingrese un numero: "))
    my_list.append(num)

highest_num = 0

for counter in range(0, len(my_list)):
    if my_list[counter] > highest_num:
        highest_num = my_list[counter]

print(my_list)
print(f"El numero mas alto fue {highest_num}.")

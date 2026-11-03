'''
2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, 
usando una para sus keys, y la otra para sus values.
'''
list_a = ['first_name', 'last_name', 'role', 'department']
list_b = ['Alek', 'Castillo', 'Software Engineer', 'Engineering']

employee_dict = {}

for key in range(0, len(list_a)):
    employee_dict[list_a[key]] = list_b[key]

print(employee_dict)
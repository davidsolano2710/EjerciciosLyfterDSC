print("--- Mayor de tres numeros ---")
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

if num1 >= num2 and num1 >= num3:
    greater = num1
elif num2 >= num1 and num2 >= num3:
    greater = num2
else:
    greater = num3

print(f"El mayor de los tres números es: {greater}")
print("--- Clasificador de edad ---")

name = input("Cual es tu nombre?: ")
last_name = input("Cual es tu apellido?: ")
age = float(input("Cual es tu edad?: "))

if age < 1:
    message = "Bebé"
elif 1 <= age < 8:
    message = "Niño"
elif 8 <= age < 12:
    message = "Preadolescente"
elif 12 <= age < 18:
    message = "Adolescente"
elif 18 <= age < 40:
    message = "Adulto joven"
elif 40 <= age < 65:
    message = "Adulto"
elif 65 <= age:
    message = "Adulto mayor"

print(f"{name} {last_name}, tu categoria es: {message}.")
print(f"Tu edad es: {age} años.")


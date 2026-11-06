import random

print("--- Juego de Adivinanza de Números ---")

random_number = random.randint(1, 10)
guess = 0

while guess != random_number:
    guess = int(input("Adivina el número entre 1 y 10: "))
    if guess == random_number:
        print("¡Felicidades! Adivinaste el número.")
    else:
        print("Intenta de nuevo.")  

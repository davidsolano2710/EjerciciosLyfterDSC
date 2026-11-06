'''
Cree una calculadora por linea de comando. Esta debe de tener un número actual,
y un menú para decidir qué operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, 
multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, 
o si ingresa un número invalido a la hora de hacer la operación.
'''

#FUNCTIONS

#UI
def menu():                       # Display the menu and get the user's option

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear result")
    print("6. Exit\n")

    while True:
        try:
            option = int(input("Select an option: "))
            if option < 1 or option > 6:                   #make sure is between 1 and 6
                raise ValueError           
            return option
        except ValueError:
            print("Error: Invalid option. Please select a valid option (1-6).")


def get_operand(option):                 # Get 2nd operand from the user, option is used to check division by zero
    while True:
        try:
            operand2 = float(input("Type opperand: "))
            if option == 4 and operand2 == 0:  # Check for division by zero
                raise ZeroDivisionError()
            else:
                return operand2
        except ValueError:
            print("Error: Invalid number. Please enter a valid number.")
        except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")


#OPERATIONS
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


#main function
def main():

    #First cycle---------------------
    #asks for two operands and an operation to perform with them

    result = 0

    while True:
        option = menu()
        if option == 6:
            print("Exiting the calculator.")
            break
        if option == 5:
            result = 0
            print("Result cleared. Current value is now:", result)
            continue
    
        operand = get_operand(option)

        match option:
            case 1:
                result = add(result, operand)
                print(f"Result: {result}\n")
            case 2:
                result = subtract(result, operand)
                print(f"Result: {result}\n")
            case 3:
                result = multiply(result, operand)
                print(f"Result: {result}\n")
            case 4:
                result = divide(result, operand)
                print(f"Result: {result}\n")


def welcome_message():
    print("Welcome to the Command Line Calculator!")


if __name__ == "__main__":
    welcome_message()
    main()
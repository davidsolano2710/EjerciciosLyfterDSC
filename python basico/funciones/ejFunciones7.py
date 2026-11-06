'''
Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
'''

def prime_numbers(numbers):
    prime_numbers_list = []

    for number in numbers:
        if number > 1:
            for i in range(2, int(number**0.5) + 1): # to check if a number is prime we need to look for factors from 2 to the sqrt of the num.
                if number % i == 0:
                    break
            else:                         #for else, when the for is not interrupted by a "break", it executes the else block(didn't now this))
                prime_numbers_list.append(number)


    return prime_numbers_list

print(prime_numbers([ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,
                     11,12,13,14,15,16,17,18,19,20,
                     21,22,23,24,25,26,27,28,29,30,
                     31,32,33,34,35,36,37,38,39,40,
                     41,42,43,44,45,46,47,48,49,50,
                     51,52,53,54,55,56,57,58,59,60,
                     61,62,63,64,65,66,67,68,69,70,
                     71,72,73,74,75,76,77,78,79,80,
                     81,82,83,84,85,86,87,88,89,90,
                     91,92,93,94,95,96,97,98,99,100]))


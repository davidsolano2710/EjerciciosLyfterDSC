def args_is_num(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):                   #isinstance() checks if the argument is a int or float.
                raise TypeError("Error: All arguments must be numbers (int or float).")
        return func(*args)
    return wrapper

      
@args_is_num
def suma(a, b):
    return a + b


@args_is_num
def print_args(*args):
    for arg in args:
        print(arg)
    print("args printed successfully")  



#tests
try:
    print(suma(10, 20))
except TypeError as e:
    print(e)

try:
    print(suma("c", 10))
except TypeError as e:
    print(e)

try:
    print_args(1,2,3,4,5,"2",7,8,9,10,11,12,13,14,15,16,17,18,19,20)
except TypeError as e:
    print(e)
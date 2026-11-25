def args_is_num(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, bool):  #in this case we wont consider boolean values as numbers
                raise TypeError("Error: Boolean values are not allowed as arguments.")
            
            if not isinstance(arg, (int, float)):                   #isinstance() checks if the argument is a int or float.
                raise TypeError("Error: All arguments must be numbers (int or float).")
            
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError("Error: All keyword arguments must be numbers (int or float).")
        return func(*args, **kwargs)
    return wrapper

      
@args_is_num
def sum_a_b(a, b):
    return a + b


@args_is_num
def print_args(*args):
    for arg in args:
        print(arg)
    print("args printed successfully")  



#tests
try:
    print(sum_a_b(True, 20))
except TypeError as e:
    print(e)

try:
    print(sum_a_b("c", 10))
except TypeError as e:
    print(e)

try:
    print_args(1,2,3,4,5,"2",7,8,9,10,11,12,13,14,15,16,17,18,19,20)
except TypeError as e:
    print(e)
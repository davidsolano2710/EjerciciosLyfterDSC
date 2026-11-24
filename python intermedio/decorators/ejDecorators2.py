def args_is_num(func):
    def wrapper(*args):
        try:
            for arg in args:
                    if not isinstance(arg, (int, float)):                   #isinstance() checks if the argument is a int or float.
                        raise ValueError
        except ValueError:
            print("Error: All arguments must be numbers (int or float).")
            return None
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
#print(suma(3, 5))
#print(suma("3", "5"))
print_args(1,2,3,4,5,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
def prmtr_rtrn_print_(func):
    def wrapper(*args):
        print(f"Function arguments: {args}")
        return_value = func(*args)
        print(f"Function return: {return_value}")
    return wrapper


@prmtr_rtrn_print_
def suma(a, b):
    return a + b

@prmtr_rtrn_print_
def print_args(*args):
    for arg in args:
        print(arg)
    return "args printed successfully"

suma(3, 5)

print_args(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
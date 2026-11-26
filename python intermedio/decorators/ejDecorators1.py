def prmtr_rtrn_print_(func):
    def wrapper(*args, **kwargs):
        print(f"Function arguments: {args}")
        return func(*args, **kwargs)                  
    return wrapper


@prmtr_rtrn_print_
def sum_a_b(a, b):
    return a + b

@prmtr_rtrn_print_
def print_args(*args):
    for arg in args:
        print(arg)
    return "args printed successfully"

suma_result = sum_a_b(3, 5)

print(suma_result)
    
print_args(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
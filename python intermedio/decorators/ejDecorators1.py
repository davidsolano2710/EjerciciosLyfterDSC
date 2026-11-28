def prmtr_rtrn_print_(func):
    def wrapper(*args, **kwargs):
        print(f"Function arguments: {args}, {kwargs}")
        func_result = func(*args, **kwargs)
        print(f"Function return value: {func_result}")
        return func(*args, **kwargs)                  
    return wrapper


@prmtr_rtrn_print_
def sum_first_two_arguments(a, b, *args, **kwargs):
    return a + b


@prmtr_rtrn_print_
def sum_all_arguments(*args):  #I didn't like the print all args method, so I changed it
    accumulator = 0
    for arg in args:
        accumulator += arg
    return accumulator

#Tests
suma_result = sum_first_two_arguments(3, 5, 7, 9, bob="example")

print(suma_result)

print(sum_all_arguments(5, 4, 3, 2, 1))

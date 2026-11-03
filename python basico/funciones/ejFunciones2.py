'''
Experimente con el concepto de scope:
    1. Intente acceder a una variable definida dentro de una función desde afuera.
    2. Intente acceder a una variable global desde una función y cambiar su valor.
'''
# 1
#--------------------------------------
def my_function():
    local_variable = 2
    return


my_function()
# print(local_variable)  error: since local_variable is defined inside my_function, we can't access it from outside the function
#--------------------------------------

# 2
#--------------------------------------
global_variable = 5

def my_function2():
    print(global_variable)                   #wont give us an error if we just want to read the value of the global variable.
    # global global_variable                 #but if we want to change the value of the global variable, we need to declare it as global,
                                             #if we don't, it will create a new local variable with the same name and won't change the global variable.
                                             # but if we access the global variable and then  
    # global_variable = global_variable + 1       
    #print(global_variable)                   
    return

my_function2()
#--------------------------------------

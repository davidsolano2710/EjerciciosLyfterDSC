from datetime import date

class User():
    def __init__(self, bd):   #bd as in birthday
        self.date_of_birth = date.fromisoformat(bd)
        
    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        # Adjust for cases where the birthday hasn't occurred yet this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years


def user_age_checker_decorator(func):
    def wrapper(*args, **kwargs):
        found_user = False
        for arg in args:
            if isinstance(arg, User):
                found_user = True
                user = arg
                break

        for key, value in kwargs.items():
            if isinstance(value, User):
                found_user = True
                user = value
                break
        
        if found_user == False:
            raise TypeError("Error: No User instance found in the arguments.")
        elif user.age < 18:
            raise ValueError("Error: User must be at least 18 years old.")
        return func(user)
    return wrapper


@user_age_checker_decorator
def user_age_info(user):
    print(f"User is {user.age} years old and can perform this action.")


@user_age_checker_decorator
def user_age_info_args(*args, **kwargs):  
    for arg in args:
        if isinstance(arg, User):
            print(f"User is {arg.age} years old and can perform this action.")
            return
    return



#tests
user1 = User('2000-01-01')
user2 = User('2010-01-01')


try:
    #user_age_info(user1)  # Should work
    user_age_info_args(1,2,3,4,5,user1)  
except (TypeError, ValueError) as e:
    print(e)

try:
    user_age_info(user2)  # Should raise a ValueError
except (TypeError, ValueError) as e:
    print(e)
try:
    user_age_info("bruh") # Should raise a TypeError
except (TypeError, ValueError) as e:   
    print(e)
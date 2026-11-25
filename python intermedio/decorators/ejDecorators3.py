from datetime import date

class User():
    def __init__(self, bd):   #bd as in birthday
        self.date_of_birth = date.fromisoformat(bd)
        

    def calculate_age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        # Adjust for cases where the birthday hasn't occurred yet this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years


def user_age_checker_decorator(func):
    def wrapper(user):
      
        if not isinstance(user, User):
            raise TypeError("Error: Argument must be an instance of the User class.")
        elif user.calculate_age() < 18:
            raise ValueError("Error: User must be at least 18 years old.")
        return func(user)
    return wrapper


@user_age_checker_decorator
def user_age_info(user):
    print(f"User is {user.calculate_age()} years old and can perform this action.")



#tests
user1 = User('2000-01-01')
user2 = User('2010-01-01')

try:
    user_age_info(user1)  # Should work
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
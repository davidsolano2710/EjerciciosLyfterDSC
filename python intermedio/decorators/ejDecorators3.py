class User():
    def __init__(self, bd, age):   #bd as in birthday
        self.date_of_birth = bd
        self.age = age


def user_age_checker_decorator(func):
    def wrapper(user):
        try:
            if not isinstance(user, User):
                    raise ValueError("Error: Argument must be an instance of the User class.")
            elif user.age < 18:
                    raise ValueError("Error: User must be at least 18 years old.")
        except ValueError as e:
            print(e)
            return 
        return func(user)
    return wrapper


@user_age_checker_decorator
def user_age_info(user):
    print(f"User is {user.age} years old and can perform this action.")


user1 = User("2000-01-01", 23)
user2 = User("2010-01-01", 13)

user_age_info(user1)  
user_age_info(user2)  
user_age_info("bruh")
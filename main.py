from views import *

class Person:
    """Create person object for authorization"""

    def __init__(self, name, user_id):
        self.name = name
        self.password = user_id


def post_name_password() -> tuple:
    name = input('Write your name: ')
    password = input('Write your password: ')
    return name, password


def main_user():
    """Authorization"""

    print('\n\n\n')
    while True:
        print('\n')
        choice = input("Choice action:\nLog in to your account - 1\n"
                       "Register new account - 2\nExit - 0\n# ")
        if choice == '1':
            name, password = post_name_password()
            userid = verify_name(name)
            if userid:
                main_person = Person(name, userid)
                print(f"The user {name} is logged in")
                break
            else:
                print('There is no such user, try again')
                continue
        elif choice == '2':
            name, password = post_name_password()
            if login_new_person(name, password):
                userid = verify_name(name)
                main_person = Person(name, userid)
                print(f'The user {name} is registered')
                break
            else:
                continue
        elif choice == '0':
            print("Catch you later!")
            break
        else:
            print("Make choice: 1, 2 or 0 for Exit")
            continue

main_user()
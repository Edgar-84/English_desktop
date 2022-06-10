from views import *


class Person:
    """Create person object with all actions"""

    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id

    def create_list(self, name: str):
        """Create new ListWord"""
        create_list_word(self.user_id, name)

    def add_word(self, name_list: str, word: str, translate: str):
        """Create new word with translate"""
        create_word(self.user_id, name_list, word, translate)

    def delete_list(self, name: str):
        """Delete ListWord with all words"""
        delete_list_word(self.user_id, name)

    def delete_word(self, list_id: str, word: str):
        """Delete word in ListWord"""
        delete_word(self.user_id, list_id, word)

    def delete_user(self):
        """Delete user with his lists and words"""
        pass

    def view_user_lists(self):
        """View all WordLists from user"""
        lists_words = view_lists_user(self.user_id)
        print(f'\n\n\nUser {self.name} have next lists:\n{lists_words}')


    def view_words_inlist(self):
        """View all words in chosen list"""
        pass

    def put_data_add_word(self) -> tuple:
        """Write info for add_word"""

        name_list = input("Enter the name of the list to store the word: \n")
        word = input("Enter word: \n")
        translate = input("Enter translate: \n")
        return name_list, word, translate

    def put_data_delete_word(self) -> tuple:
        """Write info for delete word"""

        name_list = input("Enter the name of list with word: \n")
        word = input("Enter the word from delete: \n")
        list_id = convert_list_in_id(self.user_id, name_list)
        return list_id, word


def post_name_password() -> tuple:
    """Enter user data"""

    name = input('Write your name: ')
    password = input('Write your password: ')
    return name, password


def main_user():
    """Authorization"""

    while True:
        choice = input("\n\n\nChoice action:\nLog in to your account - 1\n"
                       "Register new account - 2\nExit - 0\n# ")
        if choice == '1':
            name, password = post_name_password()
            if verify_name(name):
                userid = convert_username_toId(name)
                main_person = Person(name, userid)
                print(f"The user {name} is logged in")
                return main_person
            else:
                print('There is no such user, try again')
                continue
        elif choice == '2':
            name, password = post_name_password()
            if login_new_person(name, password):
                userid = convert_username_toId(name)
                main_person = Person(name, userid)
                print(f'The user {name} is registered')
                return main_person
            else:
                continue
        elif choice == '0':
            print("Catch you later!")
            return False
        else:
            print("Make choice: 1, 2 or 0 for Exit")
            continue



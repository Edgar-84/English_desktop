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

    def update_word(self):
        """Change word in list"""
        pass

    def update_list(self):
        """Change name list"""
        pass

    def exams_one(self):
        """Return random word and translate in list"""
        pass

    def view_user_lists(self) -> list:
        """View all WordLists from user"""
        lists_words = view_lists_user(self.user_id)
        print(f'\n\n\nUser {self.name} have next lists:\n{lists_words}')
        return lists_words

    def view_words_inlist(self, list_name: str,
                          view: bool = True, exams: bool = False,
                          first: str = 'en') -> None or dict:
        """View all words and translates in list.
            Also, can return words in dict english - russian
            or russian - english"""

        list_id = convert_list_in_id(self.user_id, list_name)

        view_words_in_list(self.user_id, list_id, view, exams, first)

    def put_data_add_word(self) -> tuple:
        """Write info for add_word"""

        word = input("Enter word: \n")
        translate = input("Enter translate: \n")
        return word, translate

    def put_data_delete_word(self, name_list: str) -> tuple:
        """Write info for delete word"""

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

            if len(name) or len(password) < 4:
                print("Write a password and name longer than 4 characters")
                continue

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

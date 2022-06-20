from views import *
import random

import openpyxl
from termcolor import cprint


def convertor_word_file(user_id: str, list_id: str) -> bool or list:
    """This converter take words and translates in file 'words'
        and put in user list"""

    book = openpyxl.open("converter/words.xlsx", read_only=True)
    sheet = book.active

    try:
        list_words = []
        for row in range(1, sheet.max_row + 1):
            info = {
                'user_id': user_id,
                'list_id': list_id,
                'word': sheet[row][0].value,
                'translate': sheet[row][1].value}
            list_words.append(info)

        return list_words
    except Exception as e:
        print("Your file with words is wrong")
        return False


def choice_while(text: str, key: str, go_back=False):
    """Wile for choice"""
    while True:
        choice = input(text)
        if choice == key:
            return True
        if go_back == True:
            if choice == '0':
                return False
        else:
            continue


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

    def downloads_from_file(self, name_list: str):
        """Download word from file 'word' """
        list_id = convert_list_in_id(self.user_id, name_list)
        list_words = convertor_word_file(self.user_id, list_id)

        if not list_words:
            return False
        else:
            downloads_words_from_file(list_words)

    def exams_one(self, list_name: str,
                  view: bool = True, exams: bool = False,
                  first: str = 'en') -> None or dict:
        """Return random word and translate in list"""

        list_id = convert_list_in_id(self.user_id, list_name)
        list_words = view_words_in_list(self.user_id, list_id, view, exams, first)
        random.shuffle(list_words)
        for word_translate in list_words:
            cprint(f'\n\n{word_translate[0]}', 'green')
            choice_while('\nPress Enter for view translate: \n# ', '')
            cprint(f'\n\n{word_translate[0]} - {word_translate[1]}', 'red')
            if not choice_while('\nPress Enter for continue or 0 for exit: \n# ',
                                '', go_back=True):
                break

    def view_user_lists(self) -> list:
        """View all WordLists from user"""
        lists_words = view_lists_user(self.user_id)
        cprint(f'\n\n\nUser {self.name} have next lists:\n{lists_words}', 'yellow')
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

        word = input("Enter word (EN): \n")
        translate = input("Enter translate (RU): \n")
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

from actions import main_user

from termcolor import cprint


def example_module(person_class: classmethod, name_list: str):
    """Work with our examples"""

    while True:
        cprint('\n\n__Examples__', 'red')
        choice = input(f'Translate English - Russian --> 1\n'
                       f'Translate Russian - English --> 2\n'
                       f'Exit --> 0\n# ')

        if choice == '1':
            person_class.exams_one(name_list, view=False, exams=True)
            continue

        elif choice == '2':
            person_class.exams_one(name_list, view=False, exams=True, first='ru')
            continue

        elif choice == '0':
            return None
        else:
            print("Make choice: 1, 2 or 0 for Exit")
            continue


def work_with_list(person_class: classmethod, name_list: str):
    """Work with chosen list"""

    while True:
        cprint(f'\n\nThe *{name_list}* list is selected.', 'red')
        choice = input(f'View words in list --> 1\n'
                       f'Add word: --> 2\n'
                       f'Delete word --> 3\n'
                       f'Delete list --> 4\n'
                       f'Run Example_1 --> 5\n'
                       f'Download list words from file "word" --> 6\n'
                       f'Exit --> 0\n# ')

        if choice == '1':
            person_class.view_words_inlist(name_list)
            continue

        elif choice == '2':
            word, translate = person_class.put_data_add_word()
            person_class.add_word(name_list, word, translate)
            continue

        elif choice == '3':
            list_id, word = person_class.put_data_delete_word(name_list)
            person_class.delete_word(list_id, word)
            continue

        elif choice == '4':
            while True:
                delete_choice = input(f"are you sure you want to delete\n"
                                      f"the list {name_list} with all words?\n"
                                      f"Yes --> 1\n"
                                      f"No --> 2\n# ")
                if delete_choice == '1':
                    person_class.delete_list(name_list)
                    return None
                elif delete_choice == '2':
                    break
                else:
                    print("Make choice: 1 or 2")

        elif choice == '5':
            example_module(person_class, name_list)
            continue

        elif choice == '6':
            person_class.downloads_from_file(name_list)
            continue

        elif choice == '0':
            return None
        else:
            print("Make choice: 1, 2, 3, 4, 5 or 0 for Exit")
            continue


def view_words_list(person_class: classmethod):
    """Interface for work with word lists"""

    while True:
        list_words = person_class.view_user_lists()
        if len(list_words) == 0:
            choice = input(f'\n\nCreate new list: --> 1\n'
                           f'Exit --> 0\n# ')
            if choice == '2':
                print("Make choice: 1 or 0 for Exit")
                continue
        else:
            choice = input(f'\n\nCreate new list: --> 1\n'
                           f'Select list --> 2\n'
                           f'Exit --> 0\n# ')
        if choice == '1':
            person_class.create_list(input("Enter name for your new list: \n# "))
            continue

        elif choice == '2':
            while True:
                number_list = input(f"Enter number list: 1... {len(list_words)}\n# ")

                if number_list not in [str(i+1) for i in range(len(list_words))]:
                    print(f"Enter number 1... {len(list_words)}")
                    continue
                else:
                    break
            name_list = list_words[int(number_list) - 1]
            work_with_list(person_class, name_list)

        elif choice == '0':
            return None
        else:
            print("Make choice: 1, 2 or 0 for Exit")
            continue


def main_menu():
    """Interface for work"""

    user = main_user()
    if user:
        while True:
            cprint(f'\n\n\nWelcome __{user.name}__', 'red')
            choice = input('Make choice:\n'
                           f'View word lists --> 1\n'
                           f'Exit --> 0\n# ')

            if choice == '1':
                view_words_list(user)

            elif choice == '0':
                print("Catch you later!")
                break
            else:
                print("Make choice: 1 or 0 for Exit")
                continue


if __name__ == '__main__':
    main_menu()

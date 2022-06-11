from actions import main_user


def main_menu():
    """Interface for work"""

    user = main_user()
    if user:
        print(user.user_id)
        while True:

            choice = input(f'\n\n\nWelcom __{user.name}__\nMake choice:\n'
                           f'Create new list: --> 1\n'
                           f'Add word: --> 2\n'
                           f'Delete word --> 3\n'
                           f'Delete list --> 4\n'
                           f'View user lists --> 5\n'
                           f'View words in list --> 6\n'
                           f'Exit --> 0\n# ')

            if choice == '1':
                user.create_list(input("Enter name for your new list: \n#"))
                continue
            elif choice == '2':
                name_list, word, translate = user.put_data_add_word()
                user.add_word(name_list, word, translate)
                continue
            elif choice == '3':
                list_id, word = user.put_data_delete_word()
                user.delete_word(list_id, word)
                continue
            elif choice == '4':
                user.delete_list(input("Enter name list for delete with all words: \n#"))
                continue
            elif choice == '5':
                user.view_user_lists()
                continue
            elif choice == '6':
                user.view_words_inlist(input("Enter name list: \n#"))
            elif choice == '0':
                print("Catch you later!")
                break
            else:
                print("Make choice: 1, 2, 3, 4, 5, 6 or 0 for Exit")
                continue


main_menu()

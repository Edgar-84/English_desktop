import os.path
import hashlib

from dotenv import load_dotenv
from models import *

load_dotenv()
PASSWORD_SALT = os.getenv("PASSWORD_SALT")


def convert_password(password: str) -> str:
    """Create hash password with PASSWORD_SALT"""

    return hashlib.sha256((password + PASSWORD_SALT).encode()).hexdigest().lower()


def verify_password(username: str, password: str) -> bool or str:
    """Verification user, checking username and
     password with hash in database"""

    if verify_name(username=username) == False:
        print("There is no such user")
        return False
    else:
        password_hash = hashlib.sha256((password + PASSWORD_SALT).encode()) \
            .hexdigest().lower()

        with db:
            stored_password_hash = User.get(User.name == username)
        if password_hash == stored_password_hash.password:
            return stored_password_hash.id
        else:
            print("Invalid password")
            return False


def verify_name(username: str) -> bool:
    """Search username in database"""

    with db:
        person_name = User.select()
        if username in [user.name for user in person_name]:
            return True
        else:
            return False


def convert_username_toId(name: str) -> bool or str:
    """Convertation username in user_id"""

    if verify_name(name) == False:
        return False
    with db:
        user_info = User.select().where(User.name == name)
        return str(*[user.id for user in user_info])


def login_new_person(name: str, password: str) -> bool:
    """Create new user"""

    if verify_name(username=name):
        print("A user with this name already exists")
        return False
    with db:
        User(name=name, password=convert_password(password)).save()
    print(f"Create new user -> {name}")
    return True


def check_listwords(user_id: str, name_list: str) -> bool:
    """Сhecking the location of the list in the database"""

    with db:
        names = ListWord.select().where(ListWord.user_id == user_id)
        if name_list in [nameList.name for nameList in names]:
            return True
        return False


def check_user_id(user_id: str) -> bool:
    """Checking user_id in table Users"""

    with db:
        users = User.select()
        if user_id in [str(user.id) for user in users]:
            return True
        return False


def create_list_word(user_id: str, name: str) -> bool:
    """Create ListWord"""

    if check_user_id(user_id) == False:
        print("Invalid user_id")
        return False

    if check_listwords(user_id, name):
        print("A list with that name already exists")
        return False
    else:
        with db:
            ListWord(user_id=user_id, name=name).save()
        print(f"Create new ListWord -> {name}")
        return True


def delete_list_word(user_id: str, name: str) -> bool:
    """Delete listword from database"""

    if check_user_id(user_id) == False:
        print("Invalid user_id")
        return False
    if check_listwords(user_id, name) == False:
        print("There is no such list")
        return False
    else:
        with db:
            list_id = convert_list_in_id(user_id, name)
            ListWord.delete().where(ListWord.user_id == user_id,
                                    ListWord.name == name).execute()

            Word.delete().where(Word.list_id == list_id).execute()
            print(f"List -> {name} is deleted")
            return True


def delete_word(user_id: str, list_id: str, word: str) -> bool:
    """Delete all words in list which we choice"""

    if checking_word(user_id, list_id, word):
        with db:
            Word.delete().where(Word.list_id == list_id, Word.user_id == user_id,
                                Word.word == word).execute()
            print(f"The word -> {word} deleted")
            return True
    else:
        print(f"The word -> {word} not find")
        return False


def convert_list_in_id(user_id: str, name: str) -> str or bool:
    """Converting the name of the list to its ID,
     provided that it exists"""
    if check_listwords(user_id, name):
        with db:
            record = (ListWord.select().where((ListWord.user_id == user_id)
                                              & (ListWord.name == name)))
            return str(*[our_record.id for our_record in record])
    else:
        print("You write wrong list")
        return False


def checking_word(user_id: str, list_id: str, word: str) -> bool:
    """Search the presence of a word in the list"""

    with db:
        our_word = (Word.select().where((Word.user_id == user_id) &
                                        (Word.list_id == list_id) &
                                        (Word.word == word)))
        if [this_word.word for this_word in our_word]:
            return True
        return False


def create_word(user_id: str, name_list: str,
                word: str, translate: str) -> bool:
    """Create new word and translate in ListWord,
    also can download word from file"""

    if check_user_id(user_id) == False:
        print("Invalid user_id")
        return False

    if check_listwords(user_id, name_list) == False:
        print("There is no such list")
        return False

    list_id = convert_list_in_id(user_id, name_list)

    if checking_word(user_id, list_id, word):
        print("This word is already on the list")
        return False

    with db:
        Word(user_id=user_id, list_id=list_id, word=word, translate=translate).save()
        print(f"""Create word -> {word}\ntranslate -> {translate}\nIn list -> {name_list}""")
        return True


def view_lists_user(user_id: str) -> list:
    """View all user lists"""

    if check_user_id(user_id) == False:
        print("Invalid user_id")
        return False

    with db:
        user_lists = ListWord.select().where(ListWord.user_id == user_id)
        return [our_list.name for our_list in user_lists]


def view_words_in_list(user_id: str, list_id: str,
                       view: bool = True, exams: bool = False,
                       first: str = 'en') -> None or dict:
    """View all words and translates in list.
        Also, can return words in dict english - russian
        or russian - english"""

    with db:
        words_translates = Word.select().where(Word.user_id == user_id,
                                               Word.list_id == list_id)

        if view == True:
            for word_transl in words_translates:
                print(word_transl.word, '-', word_transl.translate)

        if exams == True:
            if first == 'en':
                listEn_Ru = []

                for word_transl in words_translates:
                    item = list()
                    item.append(word_transl.word)
                    item.append(word_transl.translate)
                    listEn_Ru.append(item)
                return listEn_Ru

            elif first == 'ru':
                listRu_En = []

                for word_transl in words_translates:
                    item = list()
                    item.append(word_transl.translate)
                    item.append(word_transl.word)
                    listRu_En.append(item)
                return listRu_En


def downloads_words_from_file(list_words: list) -> bool:
    """Download word from file 'word'  """
    try:
        with db:
            Word.insert(list_words).execute()
        print(f"""Create word -> {list_words}""")
        return True

    except Exception as e:
        print("Download BD! Your file with words is wrong")
        return False

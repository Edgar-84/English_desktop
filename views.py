import os.path
import hashlib

from dotenv import load_dotenv
from models import *

load_dotenv()
PASSWORD_SALT = os.getenv("PASSWORD_SALT")

def convert_password(password: str) -> str:
    """Create hash password with PASSWORD_SALT"""

    return hashlib.sha256((password + PASSWORD_SALT).encode()).hexdigest().lower()


def verify_password(username: str, password: str) -> bool:
    """Verification user, checking username and
     password with hasd in database"""

    if verify_name(username=username) == False:
        print("There is no such user")
        return False
    else:
        password_hash = hashlib.sha256((password + PASSWORD_SALT).encode())\
            .hexdigest().lower()

        with db:
            stored_password_hash = User.get(User.name == username)
        if password_hash == stored_password_hash.password:
            return True
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


def login_new_person(name: str, password: str) -> bool:
    """Create new user"""

    if verify_name(username=name):
        print("A user with this name already exists")
        return False
    with db:
        new_user = User(name=name, password=convert_password(password)).save()
    print(f"Create new user -> {name}")
    return True


def check_listwords(name_list: str, user_id: str) -> bool:
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
    else:
        with db:
            new_list = ListWord(user_id=user_id, name=name).save()
        print(f"Create new ListWord -> {name}")
        return True


import datetime
from models import *


with db:
    db.create_tables([User, ListWord, Word])

print("DONE")

from peewee import *


db = SqliteDatabase('db/english.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class User(BaseModel):
    name = CharField()
    password = CharField()

    class Meta:
        db_table = 'users'


class ListWord(BaseModel):
    user_id = ForeignKeyField(User)
    name = CharField()

    class Meta:
        db_table = 'ListWords'


class Word(BaseModel):
    user_id = ForeignKeyField(User)
    list_id = ForeignKeyField(ListWord)
    word = CharField()
    translate = CharField()

    class Meta:
        db_table = 'Words'

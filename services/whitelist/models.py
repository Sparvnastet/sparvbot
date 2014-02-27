import peewee
import os

db = peewee.SqliteDatabase(os.getenv("DB_FILE"), threadlocals=True)

class Whitelist(peewee.Model):

    nick = peewee.CharField(unique=True)

    class Meta:
        database = db

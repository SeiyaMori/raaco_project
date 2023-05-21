# sql_test.py

from peewee import *

print("started")
db = MySQLDatabase("raaco", host="localhost", port=3306, user="root",
                   password="B98777%kjh!")
print("1")


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db  # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database


print("connecting...")
db.connect()
print("connected")
db.create_tables([Person, Pet])
db.close()
print("finished.")

from mongoengine import *

connect('contacts')

class User(Document):
    email = StringField(required=True)
    name = StringField(max_length=50)
    phone = StringField(max_length=200)
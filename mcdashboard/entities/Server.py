from mongoengine import (
    Document,
    StringField,
    IntegerField
)


class Server(Document):
    name = StringField(max_length=120, unique=True)
    port = IntegerField()
    container_id = StringField(max_length=1000, unique=True)
    # creator = {ReferenceField(User)}

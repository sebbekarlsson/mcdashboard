from mongoengine import (
    Document,
    StringField
)


class Server(Document):
    name = StringField(max_length=120, unique=True)
    container_id = StringField(max_length=1000, unique=True)
    # creator = {ReferenceField(User)}

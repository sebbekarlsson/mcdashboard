from mongoengine import (
    Document,
    StringField,
    IntField
)
from mcdashboard.docker_utils import client


class Server(Document):
    name = StringField(max_length=120, unique=True)
    port = IntField()
    container_id = StringField(max_length=1000, unique=True)
    # creator = {ReferenceField(User)}

    def get_container(self):
        return client.containers.get(self.container_id)

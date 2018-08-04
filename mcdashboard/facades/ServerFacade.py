from mcdashboard.entities.Server import Server
from mongoengine.queryset import DoesNotExist
from mcdashboard.docker_utils import boot_container
from mcdashboard.constants import SERVER_ID_FORMAT, DEFAULT_CONTAINER_HOST


class ServerFacade(object):
    @staticmethod
    def get(**kwargs):
        try:
            return Server.objects.get(**kwargs)
        except DoesNotExist:
            return None

    @staticmethod
    def get_all(query={}):
        return Server.objects(**query).order_by('name')

    @staticmethod
    def create(**kwargs):
        data = dict(**kwargs)

        container = boot_container(port=data['port'])
        container_id = SERVER_ID_FORMAT.format(
            container_id=container.id,
            container_host=DEFAULT_CONTAINER_HOST
        )

        data['container_id'] = container_id

        c = Server(**data)
        c.save()

        return c

    @staticmethod
    def exists(**kwargs):
        try:
            return Server.objects.get(**kwargs) is not None
        except DoesNotExist:
            return False

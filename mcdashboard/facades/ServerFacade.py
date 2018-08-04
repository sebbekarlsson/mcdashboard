from mcdashboard.entities.Server import Server
from mongoengine.queryset import DoesNotExist
from mcdashboard.docker_utils import boot_container


class ServerFacade(object):
    @staticmethod
    def get(query={}, single=False):
        if single:
            try:
                return Server.objects.get(**query)
            except DoesNotExist:
                return None

        return Server.objects(**query).order_by('name')

    @staticmethod
    def create(**kwargs):
        data = dict(**kwargs)

        container = boot_container(port=data['port'])

        data['container_id'] = container.id

        c = Server(**data)
        c.save()

        return c

    @staticmethod
    def exists(**kwargs):
        try:
            return Server.objects.get(**kwargs) is not None
        except DoesNotExist:
            return False

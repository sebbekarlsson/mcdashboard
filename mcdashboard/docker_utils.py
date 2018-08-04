import docker
import socket


client = docker.from_env()
IMAGE = 'mcserver'


def boot_container(container_id=None, port=25565):
    if container_id:
        container = client.containers.get(container_id)

        if container:
            if container.status != 'running':
                container.start()

            return container

    return client.containers.run(
        IMAGE,
        detach=True,
        environment=dict(SERVER_PORT=port),
        ports={'{}/tcp'.format(port): port}
    )


def get_free_tcp_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('', 0))
    addr, port = tcp.getsockname()
    tcp.close()
    return port

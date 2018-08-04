import docker


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

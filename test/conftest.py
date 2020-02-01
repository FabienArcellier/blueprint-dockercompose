import os
import subprocess

import pytest
import testinfra
from testcontainers.compose import DockerCompose

SCRIPT_DIR = os.path.realpath(os.path.join(__file__, '..'))
ROOT_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, '..'))


@pytest.fixture(scope="session")
def test_infra():
    docker_compose = DockerCompose(ROOT_DIR, pull=True)
    docker_compose.start()
    container = get_docker_compose_container_id('database', ROOT_DIR)
    test_infra = testinfra.get_host("docker://{}".format(container))

    yield test_infra
    docker_compose.stop()


def get_docker_compose_container_id(service: str, project_directory: str = None):
    """
    retrieves the identifier of the container that corresponds to the service

    This method only works if there is a single instance of the service in the docker-compose file.

    >>> get_docker_compose_container_id('database')
    >>> get_docker_compose_container_id('database', project_directory='/home/project')

    :param service:
    :param project_directory:
    :return:
    """
    cmd = ["docker-compose"]
    if project_directory is not None:
        cmd += [
            "--project-directory",
            "{}".format(project_directory)
        ]

    cmd += [
        "ps",
        "-q",
        service
    ]

    id = subprocess.check_output(cmd)
    return id.decode('utf-8').strip()
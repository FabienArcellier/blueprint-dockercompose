from testinfra.host import Host


def test_docker_container_expose_postgres_port(test_infra: Host):
    assert test_infra.socket("tcp://6379").is_listening

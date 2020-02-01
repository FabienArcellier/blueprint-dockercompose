# Blueprint Dockercompose

[![ci](https://github.com/FabienArcellier/blueprint-dockercompose/actions/workflows/main.yml/badge.svg)](https://github.com/FabienArcellier/blueprint-dockercompose/actions/workflows/main.yml)

Blueprint Dockercompose provides an environment to build a stack based on docker-compose.

It make easier activities as :

* organize a lab with students
* provision a developer environment for new joiners
* test a collection of images
* ...

Ce blueprint teste les containers de la stack avec `pytest` & `testinfra`.

## Getting started

* `docker-compose up` : load the docker infrastructure

## The latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/blueprint-dockercompose.git
```

### Usage with spikestarter

```bash
spike-starter --template https://github.com/FabienArcellier/blueprint-dockercompose.git myproject
```

* [spike-starter](https://pypi.org/project/spike-starter/)

## Continuous integration

more information in [.github/workflow/main.yml](.github/workflows/main.yml)

### Automatic testing on developer computer

```
poetry install
poetry run pytest
```

## References

* [Test-infra](https://github.com/philpep/testinfra)

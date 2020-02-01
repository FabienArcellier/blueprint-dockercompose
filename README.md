# Blueprint Application Docker

[![Build Status]()

A blueprint to implement docker based application

## Getting started

* `docker-compose up` : load the docker infrastructure

## The latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/blueprint-application-docker.git
```

### Usage with spikestarter

```bash
spike-starter --template https://github.com/FabienArcellier/blueprint-application-docker.git myproject
```

* [spike-starter](https://pypi.org/project/spike-starter/)

## Continuous integration

more information in [.travis.yml](.travis.yml)

### Automatic testing on developer computer

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirement-dev.txt
python -m unittest discover .
```

## References

* [Test-infra](https://github.com/philpep/testinfra)

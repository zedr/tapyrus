import yaml


def parse_yaml(path: str) -> None:
    with open(path) as fd:
        return yaml.safe_load(fd.read())

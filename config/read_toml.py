import tomli
from pprint import pp

with open('config.toml', 'br') as f:
    config = tomli.load(f)

pp(config)
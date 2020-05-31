import click

import manage_secrets


@click.group()
def entrypoint():
    pass


@entrypoint.command()
@click.option('--name', required=True,
              help='Name of parameter to get value from SSM')
def get(name):
    """get secrets"""
    print(manage_secrets.get_value_from_parameter_store(name))


if __name__ == "__main__":
    entrypoint()

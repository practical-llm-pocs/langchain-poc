import click
from src.core.main import hello as hello_function

@click.group()
def cli():
    pass

@click.command()
@click.option("-n", "--name", default='World', help="Name to say hello to.")
def hello(name):
    click.echo(hello_function(name))

cli.add_command(hello)

if __name__ == "__main__":
    cli()

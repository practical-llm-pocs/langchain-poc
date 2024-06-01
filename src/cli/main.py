import click
from dotenv import load_dotenv, find_dotenv
from src.core import hello, llama


load_dotenv(find_dotenv(".env"), override=True)
load_dotenv(find_dotenv(".env.local"), override=True)


@click.group()
def cli():
    pass

@click.command()
@click.option("-n", "--name", default='World', help="Name to say hello to.")
def say_hello(name):
    click.echo(hello(name))

@click.command()
@click.option("-p", "--prompt", default='What\'s today\'s date?', help="Ask a question.")
def ask_llama(prompt):
    click.echo(llama(prompt))

cli.add_command(say_hello, 'hello')
cli.add_command(ask_llama, 'agent')
cli.add_command(ask_llama, 'llama')

if __name__ == "__main__":
    cli()

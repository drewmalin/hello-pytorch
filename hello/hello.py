import click
import hello

@click.command()
def cli():
    click.echo('Executing PyTorch...')
    hello.printMatrix(5, 3)
import click
from hello import torch_matrix

@click.group()
@click.pass_context
@click.option('--debug/--no-debug', default=False)
def cli(ctx, debug):
    ctx.ensure_object(dict)
    ctx.obj['debug'] = debug

@cli.command()
@click.pass_context
@click.option('--width', '-w', default=3)
@click.option('--height', '-h', default=5)
def matrix(ctx, width, height):
    if ctx.obj['debug']:
        print('Executing hello')
    torch_matrix.print_basic(width, height)

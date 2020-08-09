import click
import json
from .database import db

@click.command(name='create_data')
@click.argument('data', type=click.File('rb'))
def create_data(data):
    chunk = data.read()
    new_data = json.loads(chunk.decode())
    db.insert_many(new_data)
    click.echo("created data")
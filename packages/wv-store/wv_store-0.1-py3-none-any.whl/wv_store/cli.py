import click
import requests
from pathlib import Path

API_URL = "http://127.0.0.1:8000"

@click.group()
def cli():
    pass

@cli.command()
@click.argument("file_path", type=click.Path(exists=True))
def upload_file(file_path):
    file_name = Path(file_path).name
    with open(file_path, "rb") as f:
        files = {"file": (file_name, f)}
        response = requests.post(f"{API_URL}/files/{file_name}", files=files)
    click.echo(response.json())

@cli.command()
@click.argument("file_name")
def delete_file(file_name):
    response = requests.delete(f"{API_URL}/files/{file_name}")
    click.echo(response.json())

@cli.command()
def list_files():
    response = requests.get(f"{API_URL}/files")
    click.echo(response.json())

if __name__ == "__main__":
    cli()

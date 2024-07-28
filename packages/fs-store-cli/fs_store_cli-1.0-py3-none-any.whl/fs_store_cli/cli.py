#!/usr/bin/env python3

import click
import requests
import os


@click.group()
def cli():
    pass


url = 'http://localhost:8080'


@cli.command(name='upload-file')
@click.argument('file_path', type=click.Path(exists=True))
def upload_file(file_path):
    """Upload a file to the server."""

    files = {'file': open(file_path, 'rb')}
    file_name = os.path.basename(file_path)
    try:
        response = requests.post(f"{url}/v1/files/{file_name}", files=files)
        response.raise_for_status()
        click.echo(f"File uploaded successfully. Response: {response.text}")
    except requests.exceptions.RequestException as e:
        click.echo(f"Failed to upload file: {e}", err=True)


@cli.command(name='list-files')
def list_files():
    """Get all file names from the server."""
    try:
        response = requests.get(f"{url}/v1/files")
        response.raise_for_status()
        click.echo(f"Files. Response: {response.text}")
    except requests.exceptions.RequestException as e:
        click.echo(f"Failed to upload file: {e}", err=True)


@cli.command(name='delete-file')
@click.argument('file_name')
def delete_file(file_name):
    """Delete a file from the server."""

    try:
        response = requests.delete(f"{url}/v1/files/{file_name}")
        response.raise_for_status()
        click.echo(f"File deleted successfully. Response: {response.text}")
    except requests.exceptions.RequestException as e:
        click.echo(f"Failed to upload file: {e}", err=True)


if __name__ == '__main__':
    cli()

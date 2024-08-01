import click
import os
import subprocess
import tempfile
import shutil
import ast

def find_load_model_function(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if any(decorator.attr == 'load_model' for decorator in node.decorator_list if isinstance(decorator, ast.Attribute)):
                return node.name
    return None

@click.group()
def cli():
    pass

@cli.command()
@click.argument('entry_point', type=click.Path(exists=True))
@click.option('--tag', '-t', default='backprop:latest', help='Docker image tag')
@click.option('--requirements', '-r', type=click.Path(exists=True), help='Path to requirements.txt')
def build(entry_point, tag, requirements):
    """Build a Docker image for the Backprop project, including model download."""
    click.echo(f"Building Docker image for {entry_point}")
    
    load_model_func = find_load_model_function(entry_point)
    if not load_model_func:
        click.echo("Warning: No load_model function found. The model won't be pre-downloaded.")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        shutil.copy2(entry_point, tmpdir)
        
        if requirements:
            shutil.copy2(requirements, tmpdir)
        
        download_script = f"""
import asyncio
from {os.path.splitext(os.path.basename(entry_point))[0]} import {load_model_func}

async def download_model():
    await {load_model_func}()

if __name__ == '__main__':
    asyncio.run(download_model())
"""
        with open(os.path.join(tmpdir, 'download_model.py'), 'w') as f:
            f.write(download_script)
        
        dockerfile_content = f"""
FROM python:3.9-slim

WORKDIR /app

COPY {os.path.basename(entry_point)} .
COPY download_model.py .
{"COPY requirements.txt ." if requirements else ""}

RUN pip install backprop
{"RUN pip install -r requirements.txt" if requirements else ""}

RUN python download_model.py

CMD ["python", "{os.path.basename(entry_point)}"]
"""
        with open(os.path.join(tmpdir, 'Dockerfile'), 'w') as f:
            f.write(dockerfile_content)
        
        subprocess.run(['docker', 'build', '-t', tag, tmpdir], check=True)
    
    click.echo(f"Docker image built successfully: {tag}")

if __name__ == '__main__':
    cli()

import typer

from startproject.context import FastApiProjectContext
from startproject.generator import generate_fastapi_project


app = typer.Typer(
    add_completion=False,
    help="Managing FastAPI projects made easy!",
    name="Manage FastAPI",
)


@app.command(help="Creates a FastAPI project.")
def fastapi_project(
    name: str
):
    context = FastApiProjectContext(name=name)
    generate_fastapi_project(context)


@app.command(help="Creates a Flask project.")
def flask_project(
    name: str
):
    ...
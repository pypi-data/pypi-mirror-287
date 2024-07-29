import typer
from rich import print

from picfix.commands.convert import convert_app
from picfix.commands.optimize import optimize_app
from picfix.commands.resize import resize_app

from . import __version__

app = typer.Typer(name="picfix", no_args_is_help=True, rich_markup_mode="rich")


def version_callback(value: bool):
    if value:
        print(f"picfix CLI version: [green]{__version__}[/green]")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version",
        callback=version_callback,
        is_eager=True,
    ),
):
    return


app.add_typer(
    resize_app,
    name="resize",
    help="resize images to specified dimensions",
    no_args_is_help=True,
)
app.add_typer(
    convert_app, name="convert", help="convert image formats", no_args_is_help=True
)
app.add_typer(
    optimize_app,
    name="optimize",
    help="optimize images to reduce file size",
    no_args_is_help=True,
)

if __name__ == "__main__":
    app()

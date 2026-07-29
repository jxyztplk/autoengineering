from __future__ import annotations

import typer

app = typer.Typer(
    name="autoeng",
    help="Evaluate software changes through controlled experiments.",
    no_args_is_help=True,
)

hypothesis_app = typer.Typer(help="Manage hypotheses.")
experiment_app = typer.Typer(help="Manage experiments.")
repository_app = typer.Typer(help="Inspect the target repository.")

app.add_typer(hypothesis_app, name="hypothesis")
app.add_typer(experiment_app, name="experiment")
app.add_typer(repository_app, name="repo")


@app.command()
def version() -> None:
    """Print the Auto-Engineering version."""
    typer.echo("0.1.0")


def main() -> None:
    app()

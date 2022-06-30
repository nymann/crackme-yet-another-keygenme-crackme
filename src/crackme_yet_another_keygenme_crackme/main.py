import typer

app = typer.Typer()


@app.command()
def keygen() -> None:
    typer.echo("Implement your keygen for crackme_yet_another_keygenme_crackme here.")


if __name__ == "__main__":
    app()

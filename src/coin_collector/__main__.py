import typer
from .game import run_game

app = typer.Typer()

@app.command()
def play(
    levels: list[str] = typer.Argument(..., help="Liste der Level-Dateien (JSON)"),
    fps: int = 60,
    debug: bool = False
):
    """Startet das Coin Collector Spiel mit den angegebenen Leveln."""
    run_game(levels, fps, debug)

if __name__ == "__main__":
    app()
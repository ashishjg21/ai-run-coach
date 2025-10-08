import typer
from backend.app import crud

app = typer.Typer()

@app.command()
def logrun(distance: float, pace: str, rpe: int = 5, notes: str = ""):
    run = crud.add_run(distance, pace, rpe, notes)
    print(f"Run logged: {run.distance} km at {run.pace}, RPE {run.rpe}, notes: {run.notes}")

if __name__ == "__main__":
    app()

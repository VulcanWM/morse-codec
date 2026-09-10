import typer
from morse import encode_file

app = typer.Typer()

@app.command()
def encode(text: str, file_name: str):
    encode_file(text, file_name)
    print(f"Done! Check {file_name}")


@app.command()
def decode(file_name: str):
    print("Not worked on yet.")

if __name__ == "__main__":
    app()

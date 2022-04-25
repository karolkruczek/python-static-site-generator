import typer
from ssg.site import Site

def main(source, dest):
    config = {
        "source": source,
        "dest": dest
        }
    Site(**config).build()

typer.run(main)
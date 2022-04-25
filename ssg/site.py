from os import mkdir
from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path()
        self.dest = Path()

    def create_dir(self, path):
        directory  = self.dest + "/" + self.source.relative_to()
        mkdir(directory,parents = True, exist_ok = True)

    def build(self):
        for path in self.source.rglob("*"):
            if path == self.directory:
                self.create_dir(path)



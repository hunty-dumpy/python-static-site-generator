from typing import List
from pathlib import Path
import shutil


class Parser:
    extensions : List[str] = []

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, 'r') as file:
            return file.read()

    def write(self, path, dest, content, ext = ".html"):
        full_path = self.dest / path.with_suffix(ext).name   # other forks show teh solution using only dest insteald of self.dest as mentioned in the instructions.
        with open(full_path, 'w') as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        super().copy(path, source, dest)

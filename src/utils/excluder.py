from pathlib import Path
import shutil

class Excluder:
    def __init__(self, path: str):
        self.path = Path(path)

    def clear_contents(self) -> None:
        for item in self.path.iterdir():
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)

    
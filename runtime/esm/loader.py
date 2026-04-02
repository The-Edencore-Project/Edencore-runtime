# ESM Loader - connects Runtime to the Silicon Model repo

from silicon_model.loader import SiliconMindLoader

class ESMLoader:
    def __init__(self):
        self.loader = SiliconMindLoader()

    def load(self, path):
        return self.loader.load(path)
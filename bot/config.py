from pathlib import Path
import yaml

class Config:
    def __init__(self):
        config_path = Path("configuration.yaml")
        with open(config_path, "r") as f:
            self.data = yaml.safe_load(f)

    def get(self, key, default=None):
        return self.data.get(key, default)

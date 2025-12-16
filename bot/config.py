import yaml

class Config:
    def __init__(self):
        with open("configuration.yaml", "r") as f:
            data = yaml.safe_load(f)

        self.bot_token = data["bot_token"]

from pathlib import Path
from typing import Self, Any

class Config:
    _isInstance = None
    _dictionary = {}

    def __new__(cls) -> Any | Self:
        if cls._isInstance is None:
            cls._isInstance = super(Config, cls).__new__(cls)

            config_path = Path(__file__).parents[4] / "resources" / "urls.properties"

            if not config_path.exists():
                raise FileNotFoundError("Path was not found")

            with open(config_path, "r") as file:
                for i in file:
                    if "=" in i:
                        key,value = i.split("=")
                        cls._dictionary[key] = value.strip()

        return cls._isInstance

    @staticmethod
    def fetch(key: str, default_value: Any = None) -> Any:
        return Config()._dictionary.get(key, default_value)
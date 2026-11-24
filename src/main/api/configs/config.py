
import os
from pathlib import Path
from typing import Any, Self


class Config:
    _instance = None
    _dictionary = {}

    def __new__(cls) -> Any | Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            config_path = Path(__file__).parents[4] / "resources" / "urls.properties"

            if not config_path.exists():
                raise FileNotFoundError(f"Config file not found: {config_path}")

            with open(config_path, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()

                    if not line or line.startswith("#") or "=" not in line:
                        continue

                    key, value = line.split("=", 1)
                    cls._dictionary[key.strip()] = value.strip()

            for env_name, env_value in os.environ.items():
                normalized_env_name = env_name.casefold().replace("_", "")

                for key in cls._dictionary:
                    normalized_key = key.casefold().replace("_", "")

                    if normalized_key == normalized_env_name:
                        cls._dictionary[key] = env_value

        return cls._instance

    @staticmethod
    def fetch(key: str, default_value: Any = None) -> Any:
        config = Config()
        return config._dictionary.get(key, default_value)

# TODO: read in your yaml file and parse it using the data classes defined in dataclasses.py
from pathlib import Path
import yaml
from nba.dataclasses import Config


def load_config() -> Config:
    # Locate config.yaml in the repository root and Read YAML into a Python dictionary
    config_path = Path(__file__).resolve().parent.parent / "config.yaml"
    raw_config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    """
    yaml.safe_load read the yaml file and added to the python dictionary
    """

    # Validate and convert the configuration
    config = Config.model_validate(raw_config)

    # Resolve the data path relative to config.yaml
    if not config.data.data_path.is_absolute():
        config.data.data_path = (
            config_path.parent / config.data.data_path
        ).resolve()

    return config
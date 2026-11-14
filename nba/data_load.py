import pandas as pd
from pathlib import Path
from nba.config import load_config


def load_csv(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path)


if __name__ == "__main__":
    config = load_config()
    data_path = config.data.data_path
    df = load_csv(data_path)
    print(data_path)

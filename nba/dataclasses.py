# TODO: define your data classes here
from pathlib import Path
from pydantic import BaseModel


class DataConfig(BaseModel):
    table: str
    data_path: Path
    features_columns: list[str]


class ModelParams(BaseModel):
    max_iter: int
    random_state: int


class ModelConfig(BaseModel):
    name: str
    type: str
    params: ModelParams


class Config(BaseModel):
    data: DataConfig
    model: ModelConfig
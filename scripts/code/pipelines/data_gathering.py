import pandas as pd
from code.logging import logger  # Importing logger module for logging

class DataGathering:
    def __init__(self, config: dict) -> None:
        self.config = config

    def run(self) -> pd.DataFrame:
        logger.info("Reading input data")
        return pd.read_csv(self.config['paths']['data_path'])
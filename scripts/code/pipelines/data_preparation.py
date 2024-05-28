import pandas as pd
from sklearn.model_selection import train_test_split
from code.logging import logger  # Importing logger module for logging

class DataPreparation:
    def __init__(self, config: dict) -> None:
        self.config = config

    def run(self, df: pd.DataFrame):
        logger.info("Preparing the data for model training")
        X = df.drop(columns=['target'], axis=0)
        y = df['target']
        return train_test_split(X,y)
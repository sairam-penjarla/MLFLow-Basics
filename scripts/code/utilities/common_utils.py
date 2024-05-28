import pickle
from code.logging import logger  # Importing logger module for logging

class CommonUtils:
    def __init__(self, config) -> None:
        self.config = config

    def save_model_to_pickle(self, model):
        filename = self.config['paths']['model_pkl_path']
        with open(filename, 'wb') as file:
            pickle.dump(model, file)
        logger.info(f"Model saved to {filename}")
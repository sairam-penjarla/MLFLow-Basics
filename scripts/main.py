from code.config import read_config
from code.pipelines.data_gathering import DataGathering
from code.pipelines.data_preparation import DataPreparation
from code.pipelines.model_training import ModelTraining

config = read_config()

data_gathering = DataGathering(config)
data_preparation = DataPreparation(config)
model_training = ModelTraining(config)

df = data_gathering.run()
X_train, X_test, y_train, y_test = data_preparation.run(df)
model_training.run(X_train, X_test, y_train, y_test)
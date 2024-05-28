import mlflow
import numpy as np
import pandas as pd
import mlflow.sklearn
from code.utilities.common_utils import CommonUtils
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from code.logging import logger  # Importing logger module for logging

class ModelTraining():
    def __init__(self, config: dict) -> None:
        self.config = config
        self.utils = CommonUtils(config)

    def run(self, X_train : pd.DataFrame, X_test : pd.DataFrame, y_train : pd.DataFrame, y_test : pd.DataFrame) -> None:
        with mlflow.start_run() as run:
            run_id = run.info.run_id
            logger.info(f"Run ID: {run_id}")
            
            # Model initialisation
            logger.info("Initialising model")
            params = self.config['params']['random_forest_regressor_params']
            mlflow.log_params(params)
            rf = RandomForestRegressor(**params)
            
            # Train model
            logger.info("Training Model")
            rf.fit(X_train, y_train)
            self.utils.save_model_to_pickle(rf) # Save model to pickle file
            mlflow.sklearn.log_model(rf, "Random Forest Regressor Model") # Log model to mlflow
            
            # Predict and evaluate
            logger.info("Calculating metrics")
            predictions = rf.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            r2 = r2_score(y_test, predictions)
            
            # Log metrics to mlflow
            mlflow.log_metric("mse", mse)
            mlflow.log_metric("r2", r2)
            
            # For example, a plot of predicted vs true values
            logger.info("Plotting scatter plot")
            plt.figure(figsize=(10,6))
            plt.scatter(y_test, predictions)
            plt.xlabel("True Values")
            plt.ylabel("Predictions")
            plt.title("True vs Predictions")
            plot_path = self.config['paths']['plot_path']
            plt.savefig(plot_path)
            mlflow.log_artifact(plot_path)
            
            # Log feature importance
            logger.info("Logging artifacts to mlflow")
            feature_importance = rf.feature_importances_
            importance_df = pd.DataFrame({
                "feature": X_train.columns,
                "importance": feature_importance
            }).sort_values(by="importance", ascending=False)
            importance_csv_path = self.config['paths']['feature_imp_path']
            importance_df.to_csv(importance_csv_path, index=False)
            mlflow.log_artifact(importance_csv_path)
            
            # Optionally, log the training and test datasets
            artifacts_path = self.config['paths']['artifacts_path']
            np.savetxt(artifacts_path + r"/X_train.csv", X_train, delimiter=",")
            np.savetxt(artifacts_path + r"/X_test.csv", X_test, delimiter=",")
            np.savetxt(artifacts_path + r"/y_train.csv", y_train, delimiter=",")
            np.savetxt(artifacts_path + r"/y_test.csv", y_test, delimiter=",")
            mlflow.log_artifact(artifacts_path + r"/X_train.csv")
            mlflow.log_artifact(artifacts_path + r"/X_test.csv")
            mlflow.log_artifact(artifacts_path + r"/y_train.csv")
            mlflow.log_artifact(artifacts_path + r"/y_test.csv")
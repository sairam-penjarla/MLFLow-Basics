# MLflow Demo Project

## Overview

This project is aimed at demonstrating the basic functionality of MLflow. It provides a practical example of how to use MLflow with a Random Forest Regressor applied to a diabetes dataset.

## Contents

- **`Demo.ipynb`**: Located in the `scripts` folder, this Jupyter notebook provides a comprehensive overview and step-by-step walkthrough of the entire code.
- **Python Scripts**: The same code from the notebook has been restructured and streamlined into multiple `.py` files with classes, methods, and functions for better organization and reusability.

## Project Details

- **Model**: Random Forest Regressor
- **Dataset**: Diabetes dataset
- **Target Variable**: `target`
- **Evaluation Metrics**: Mean Squared Error (MSE) and R-Squared

## Simplifications

For simplicity, the project does not focus on:
- Feature validation
- Feature engineering
- Feature scaling
- Feature encoding

## Instructions

1. **Initial Setup**:
   - The `scripts` folder does not contain the `mlruns` folder initially.
   
2. **Run the Main Script**:
   - Execute the `main.py` file.
   - A folder named `mlruns` will be created automatically, containing all runs and their artifacts, parameters.

3. **MLflow UI**:
   - To visualize the MLflow runs, execute the following command:
     ```bash
     mlflow ui --port 8080
     ```
   - This will launch the MLflow UI on port 8080.

## Highlights

- **Code Quality**:
  - Well-commented code
  - Logging for better traceability
  - Structured code with class abstraction
  - Reusable utilities
  - Comprehensive documentation

Explore the repository to understand the structured approach towards implementing machine learning models with MLflow tracking.
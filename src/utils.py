import os
import sys
import numpy as np
import pandas as pd

import dill
import pickle

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException



def save_object(file_path, obj):
    """
    Saves a Python object to a file using pickle serialization.

    Args:
        file_path (str): Path to the file where the object will be saved.
        obj: Python object to be saved.

    Raises:
        CustomException: If an error occurs during object serialization or file writing.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)



def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Evaluates machine learning models using grid search and reports performance metrics.

    Args:
        X_train (array-like): Feature matrix of the training data.
        y_train (array-like): Target values of the training data.
        X_test (array-like): Feature matrix of the testing data.
        y_test (array-like): Target values of the testing data.
        models (dict): Dictionary containing machine learning models to be evaluated.
        param (dict): Dictionary containing hyperparameters for each model.

    Returns:
        dict: A dictionary containing the performance scores of each model on the testing data.

    Raises:
        CustomException: If an error occurs during model evaluation.
    """
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)



def load_object(file_path):
    """
    Loads a Python object from a file.

    Args:
        file_path (str): Path to the file containing the object to be loaded.

    Returns:
        obj: The Python object loaded from the file.

    Raises:
        CustomException: If an error occurs during object deserialization or file reading.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)

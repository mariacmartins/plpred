from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.base import BaseEstimator
import pickle
import pandas as pd
import numpy as np

class PlpredModel:
    def __init__(self, estimator:BaseEstimator=RandomForestClassifier()) -> None:
        """
        Initialize the object.

        Parameters
        ---------
        estimator: BaseEstimator.
            A sckit-learn estimator

        Returns
        -------
            None
        """
        self.estimator = estimator
    
    def fit(self, X:pd.DataFrame, y:pd.Series) -> None:
        """
        Fits the underlying estimator.

        Parameters
        ---------
        X: pd.DataFrame
            features
        y: pd.Series
            labels

        Returns
        -------
            None
        """
        self.estimator.fit(X, y)

    def predict(self, X:pd.DataFrame) -> np.array:
        """
        Generates a prediction based on the underlying fitted model.

        Parameters
        ---------
        X: pd.DataFrame
            features

        Returns
        -------
        y_pred: np.array
            labels
        """
        y_pred = self.estimator.predict(X)
        return y_pred

    def validate(self, X_test:pd.DataFrame, y_test:pd.Series) -> str:
        """
        Validates the model using test data.

        Parameters
        ---------
        X_test: pd.DataFrame
            features
        y_test: pd.Series
            labels

        Returns
        -------
        report: str
            report with the main classification metrics.
        """
        y_pred = self.predict(X_test)
        report = classification_report(y_test, y_pred)
        return report

    def save(self, file_path:str) -> None:
        """
        Saves the model to a serialized pickle file.

        Parameters
        ---------
        file_path: str
            path to the output file.

        Returns
        -------
            None
        """
        with open(file_path, 'wb') as handle:
            pickle.dump(self, handle)


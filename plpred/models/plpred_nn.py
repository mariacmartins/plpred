from .base_model import BaseModel
from sklearn.neural_network import MLPClassifier

class PlpredNN(BaseModel):
    def __init__(self):
        self.estimator = MLPClassifier()
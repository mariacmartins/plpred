from .base_model import BaseModel
from sklearn.ensemble import RandomForestClassifier

class PlpredRF(BaseModel):
    def __init__(self):
        self.estimator = RandomForestClassifier()
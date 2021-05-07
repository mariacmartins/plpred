from .base_model import BaseModel
from sklearn.svm import SVC

class PlpredSVM(BaseModel):
    def __init__(self):
        self.estimator = SVC()
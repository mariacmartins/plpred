# Plpred

By Maria Clara Martins

A protein subcellular location prediction program

## Setup

```
$ make setup
```

## 📁 Project Structure

- `environment.yml`: Environment configuration file.
- `requirements.txt`: Libs needed for the project.
- `Makefile`: Create "rules" to centralize and execute main commands.
- `plpred`: Main package directory, with application functions.
- `data/`: Data directory. Raw data are saved in `data/raw`, preprocessed data in `data/processed` and trained models are saved in `data/models` (models are serialized using pickle).
- `plpred/models`: provides predictive models based on **Random Forest, Gradient Boosting, Neural Networks (MLP) and SVM.**
- `tests/`: set of unit tests for Plpred components.

## Machine Learning - Models description

**RandomForestClassifier**:
A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. 

**GradientBoostingClassifier**:
GB builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions.

**MLPClassifier**:
Multi-layer Perceptron classifier. This model optimizes the log-loss function using LBFGS or stochastic gradient descent.

**C-Support Vector Classification**:
The implementation is based on libsvm. The fit time scales at least quadratically with the number of samples and may be impractical beyond tens of thousands of samples. 


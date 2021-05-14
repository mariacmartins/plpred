from plpred.preprocessing import generate_aa_composition_df
from plpred.models import PlpredGB, PlpredNN, PlpredRF, PlpredSVM
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score
import pandas as pd
import tempfile
import os

df_membrane = generate_aa_composition_df('data/raw/membrane.fasta', membrane_label=1)
df_cytoplasm = generate_aa_composition_df('data/raw/cytoplasm.fasta', membrane_label=0)
df_processed = pd.concat([df_membrane, df_cytoplasm])

X = df_processed.drop(['membrane'], axis=1)
y = df_processed['membrane']

X_train, X_test, y_train, y_test = train_test_split(X, y)

# PlpredGB
def test_plpredgb_fit():
    model = PlpredGB()
    model.fit(X_train, y_train)

def test_plpredgb_predict():
    model = PlpredGB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

def test_plpredgb_accuracy():
    model = PlpredGB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    assert accuracy_score(y_test, y_pred) >= 0.8

def test_plpredgb_recall():
    model = PlpredGB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    assert recall_score(y_test, y_pred) >= 0.8

def test_plpredgb_save():
    model = PlpredGB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    tempfile_path = tempfile.NamedTemporaryFile().name
    model.save(tempfile_path)
    assert os.path.isfile(tempfile_path)

# PlpredNN
def test_plprednn_fit():
    model = PlpredNN()
    model.fit(X_train, y_train)

def test_plprednn_predict():
    model = PlpredNN()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

def test_plprednn_accuracy():
    model = PlpredNN()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    assert accuracy_score(y_test, y_pred) >= 0.8

def test_plprednn_recall():
    model = PlpredNN()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    assert recall_score(y_test, y_pred) >= 0.8

def test_plprednn_save():
    model = PlpredNN()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    tempfile_path = tempfile.NamedTemporaryFile().name
    model.save(tempfile_path)
    assert os.path.isfile(tempfile_path)


# PlpredRF
def test_plpredrf_fit():
    model = PlpredRF()
    model.fit(X_train, y_train)

def test_plpredrf_predict():
    model = PlpredRF()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

def test_plpredrf_accuracy():
    model = PlpredRF()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    assert accuracy_score(y_test, y_pred) >= 0.8

def test_plpredrf_recall():
    model = PlpredRF()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    assert recall_score(y_test, y_pred) >= 0.8

def test_plpredrf_save():
    model = PlpredRF()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    tempfile_path = tempfile.NamedTemporaryFile().name
    model.save(tempfile_path)
    assert os.path.isfile(tempfile_path)

# PlpredSVM
def test_plpredsvm_fit():
    model = PlpredSVM()
    model.fit(X_train, y_train)

def test_plpredsvm_predict():
    model = PlpredSVM()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

def test_plpredsvm_accuracy():
    model = PlpredSVM()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    assert accuracy_score(y_test, y_pred) >= 0.8

def test_plpredsvm_recall():
    model = PlpredSVM()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    assert recall_score(y_test, y_pred) >= 0.8

def test_plpredsvm_save():
    model = PlpredSVM()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    tempfile_path = tempfile.NamedTemporaryFile().name
    model.save(tempfile_path)
    assert os.path.isfile(tempfile_path)
from plpred.preprocessing import compute_aa_composition
from celery import Celery
from dotenv import load_dotenv
import pandas as pd
import pickle
import os

try:
    load_dotenv()
except:
    pass

redis_uri = os.environ['REDIS_URI']
celery = Celery(__name__, broker=redis_uri, backend=redis_uri)
model = pickle.load(open('data/models/model.pickle', 'rb'))

@celery.task()
def predict_protein_location(protein_sequence: str) -> str:
    aa_composition = compute_aa_composition(protein_sequence)
    df_aa_composition = pd.DataFrame([aa_composition])
    prediction = model.predict(df_aa_composition)

    if prediction == 1:
        protein_location = 'membrane'
    else:
        protein_location = 'cytoplasm'

    return protein_location
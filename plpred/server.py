from flask import Flask, render_template, request
from plpred.preprocessing import compute_aa_composition
import pandas as pd
import pickle
import argparse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    protein_sequence = request.form.get('protein_sequence')
    aa_composition = compute_aa_composition(protein_sequence)
    df_aa_composition = pd.DataFrame([aa_composition])
    prediction = app.config['model'].predict(df_aa_composition)

    if prediction == 1:
        protein_location = 'membrane'
    else:
        protein_location = 'cytoplasm'

    return render_template('index.html', protein_location=protein_location)

def main():
    argument_parser = argparse.ArgumentParser(description='plpred-server: subcellular location prediction server')
    argument_parser.add_argument('-H', '--host', required=True, help='host adress')
    argument_parser.add_argument('-p', '--port', required=True, help='host port')
    argument_parser.add_argument('-m', '--model', required=True, help='trained model to be deployed')
    arguments = argument_parser.parse_args()
        
    with open(arguments.model, 'rb') as handle:
        app.config['model'] = pickle.load(handle)


    app.run(host=arguments.host, port=arguments.port)

if __name__ == '__main__':
    main()

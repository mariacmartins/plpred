from flask import Flask, render_template, request, redirect
from celery.result import AsyncResult
from plpred.worker import celery, predict_protein_location
import pandas as pd
import argparse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    protein_sequence = request.form.get('protein_sequence')
    job_id = predict_protein_location.apply_async((protein_sequence,))
    return redirect(f'/results/{job_id}')

@app.route('/results/<job_id>', methods=['GET'])
def results(job_id:str):
    job_result = AsyncResult(job_id, app=celery)
    return render_template('results.html', job_result=job_result)

def main():
    argument_parser = argparse.ArgumentParser(description='plpred-server: subcellular location prediction server')
    argument_parser.add_argument('-H', '--host', required=True, help='host adress')
    argument_parser.add_argument('-p', '--port', required=True, help='host port')
    arguments = argument_parser.parse_args()
        
    app.run(host=arguments.host, port=arguments.port)

if __name__ == '__main__':
    main()

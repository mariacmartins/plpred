from plpred.preprocessing import compute_aa_composition
from Bio import SeqIO
import pandas as pd
import argparse
import pickle

def run_model(file_path: str, model_path: str) -> pd.DataFrame:
    """
    Run a membrane protein prediction on a FASTA file.

    Parameters
    ----------
    file_path: str
        path to proteins in FASTA format.

    model_path: str
        path to trained model in pickle format.

    Returns
    -------
    df_prediction: pd.DataFrame
        Pandas DataFrame containing the membrane proteins predictions.
    """
    with open(model_path, 'rb') as handle:
        model = pickle.load(handle)

    handle = open(file_path)
    parser = SeqIO.parse(handle, 'fasta')

    df_aa_composition = pd.DataFrame()
    df_predictions = pd.DataFrame(columns=['id', 'membrane'])

    for record in parser:
        aa_composition = compute_aa_composition(str(record.seq))
        aa_composition['id'] = record.id
        df_aa_composition = df_aa_composition.append(aa_composition, ignore_index=True)

    X = df_aa_composition.drop(['id'], axis=1)
    ids = df_aa_composition['id']
    y_pred = model.predict(X)

    df_predictions['id'] = ids
    df_predictions['membrane'] = y_pred

    return df_predictions


def main():
    argument_parser = argparse.ArgumentParser(description='plpred-predict: subcellular location prediction tool')
    argument_parser.add_argument('-i', '--input', required=True, help='input file (.fasta)')
    argument_parser.add_argument('-o', '--output', required=True, help='output file (.csv)')
    argument_parser.add_argument('-m', '--model', required=True, help='trained model (.pickle)')
    
    arguments = argument_parser.parse_args()

    df_predictions = run_model(file_path=arguments.input, model_path=arguments.model)
    df_predictions.to_csv(arguments.output, index=False)

if __name__ == '__main__':
    main()


from Bio import SeqIO
from Bio.SeqUtils import ProtParam
import pandas as pd

def compute_aa_composition(protein_sequence:str) -> dict:
    """
    Computes the aminoacid composition of a given protein sequence.

    Parameters
    ----------
    protein_sequence: str
      sequence of the protein to be processed
    
    Returns
    -------
    aa_composition: dict
      dictionary containing the relative abundance of each aminoacid

    """

    analyzer = ProtParam.ProteinAnalysis(str(protein_sequence))
    aa_composition = analyzer.get_amino_acids_percent()
    return aa_composition

def generate_aa_composition_df(file_path:str, membrane_label:int) -> pd.DataFrame:
    """
    Generates a Pandas DataFrame containing the amino acid composition for each protein
    in an FASTA file

    Parameters
    ----------
    file_path: str
      FASTA file to be processed
    
    membrane_label: int
      label indicating if the protein is located in the membrane (1) of cytoplasm (0)
    
    Returns
    -------
    df: pd.DataFrame
      DataFrame containing the amino acid composition

    """

    df = pd.DataFrame()
    handle = open(file_path)
    parser = SeqIO.parse(handle, 'fasta')

    for protein in parser:
        protein_data = compute_aa_composition(protein.seq)
        protein_data['membrane'] = membrane_label
        df = df.append([protein_data], ignore_index=True)
    
    return df

if __name__ == "__main__":

    print('processing FASTA file: membrane proteins')
    df_membrane = generate_aa_composition_df(file_path='data/raw/membrane.fasta', membrane_label=1)
    
    print('processing FASTA file: cytoplasm proteins')
    df_cytoplasm = generate_aa_composition_df(file_path='data/raw/cytoplasm.fasta', membrane_label=0)

    df_processed = pd.concat([df_membrane, df_cytoplasm])
    
    print('Saving processed DataFrame to file')
    df_processed.to_csv('data/processed/processed.csv', index=False)
    
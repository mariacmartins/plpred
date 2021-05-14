from plpred.preprocessing import compute_aa_composition, generate_aa_composition_df

def test_compute_aa_composition_result_simple_homopolymer():
    protein_sequence = 'AAAAAA'
    aa_composition = compute_aa_composition(protein_sequence)
    assert aa_composition['A'] == 1

def test_compute_aa_composition_result_complex_heteropolymer():
    protein_sequence = 'AWGY'
    aa_composition = compute_aa_composition(protein_sequence)
    assert aa_composition['A'] == 0.25
    assert aa_composition['W'] == 0.25
    assert aa_composition['G'] == 0.25
    assert aa_composition['Y'] == 0.25

def test_compute_aa_composition_return_type():
    protein_sequence = 'AWGY'
    aa_composition = compute_aa_composition(protein_sequence)
    assert isinstance(aa_composition, dict)

def test_generate_aa_composition_df_column_number():
    file_path = 'data/raw/membrane.fasta'
    df_aa_composition = generate_aa_composition_df(file_path, membrane_label=1)
    assert df_aa_composition.shape[1] == 21

def test_generate_aa_composition_df_membrane_column():
    file_path = 'data/raw/membrane.fasta'
    df_aa_composition = generate_aa_composition_df(file_path, membrane_label=1)
    assert 'membrane' in df_aa_composition.columns

def test_generate_aa_composition_df_membrane_column_values():
    file_path = 'data/raw/membrane.fasta'
    membrane_labels = [0, 1, 2, 3, 4]
    for membrane_label in membrane_labels:
        df_aa_composition = generate_aa_composition_df(file_path, membrane_label=membrane_label)
        assert all(df_aa_composition['membrane'] == membrane_label)
   
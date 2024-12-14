
def extract_rna_sequences(rna_sequence):
    """
    1. Find starting codon (AUG - Methyonin)
    2. get trimer by increasing the index by 3
    3. When we see termination codon (UAG, UAA, UGA), append that codon for the last and break.
    4. Return the RNA sequence we made

    We'll return a single sequence while this is a merged sequence of several RNAs. 
    It's ok until now since we'll only look for trimers.
    """
    termination_codons = {'ATC', 'UAG', 'ATT', 'UAA', 'ACT' 'UGA'}
    extracted_sequence = ''  # List to store RNA sequences

    i = 0
    while i < len(rna_sequence) - 2:
        codon = rna_sequence[i:i+3]
        if codon in ['AUG', 'TAC']:  # Found a start codon
            start_idx = i
            while i < len(rna_sequence) - 2:
                codon = rna_sequence[i:i+3]
                if codon in termination_codons:  # Found a termination codon
                    # Add the sequence from start codon to termination codon
                    extracted_sequence += rna_sequence[start_idx:i+3]
                    break
                i += 3
            else:
                # If no termination codon is found, exit the loop
                break
        i += 1

    return extracted_sequence
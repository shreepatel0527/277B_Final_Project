import numpy as np 

# this py file one hot encodes a string of RNA sequence and returns a (len, 4) array

def onehote(sequence, max_len):
    # map each nucelotide in the string as a number 
    mapping = {"A": 0, "C": 1, "G": 2, "T": 3, "U": 3}

    one_hot_encoded = []

    if len(sequence) > max_len: # Adjust according to your expected sequence size
        print(f"Skipping long sequence of length {len(sequence)}")
        return None

    for nuc in sequence:
        # Check if nucleotide is valid 
        if nuc in mapping:

            encoded = np.eye(4)[mapping[nuc]]  
            one_hot_encoded.append(encoded) 
        else:
            # If nucleotide is not valid, skip it
            print(f"Warning: Invalid nucleotide '{nuc}' encountered. Skipping.")
            return None
        
    return np.array(one_hot_encoded)

import numpy as np

def one_hot_signal(sequence):
    """
    Generate one-hot signal vectors for a nucleotide sequence.
    Each nucleotide (A, T, C, G) gets its own binary signal vector.
    """
    # Define the mapping for nucleotides
    mapping = {"A": 0, "C": 1, "G": 2, "T": 3, "U": 3}
    
    # Initialize signals
    signals = np.zeros((4, len(sequence)), dtype=int)  # 4 rows for A, T, C, G
    
    for i, nucleotide in enumerate(sequence):
        if nucleotide in mapping:
            signals[mapping[nucleotide], i] = 1
        else:
            print(f"Warning: Invalid nucleotide '{nucleotide}' encountered. Skipping.")
            return None            

    return signals

def process_sequences(sequences, y, max_len):
    """
    Process multiple sequences to form a stack of signal matrices with padding.
    """
    signal_matrices = []
    updated_y = []

    for i, seq in enumerate(sequences):
        # Generate the signal matrix for the current sequence
        signal_matrix = one_hot_signal(seq)

        if signal_matrix is not None:
            # Pad the signal matrix to the max length
            padded_signal = np.pad(
                signal_matrix, 
                pad_width=((0, 0), (0, max_len - signal_matrix.shape[1])), 
                mode='constant', 
                constant_values=0
            )

            # Append to the list
            signal_matrices.append(padded_signal)
            updated_y.append(y[i])

    # Stack all matrices into one array (3D array)
    all_signals = np.stack(signal_matrices, axis=0)  # Shape: (num_sequences, 4, max_seq_length)
    return all_signals, np.array(updated_y)

# usage example 

dna='ATTTACGGATTGCTGA'
#calling onehote function
oneHotEncodedDna= onehote(dna, 3)
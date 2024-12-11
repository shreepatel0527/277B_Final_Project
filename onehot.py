import numpy as np 

# this py file one hot encodes a string of RNA sequence and returns a (len, 4) array

def onehote(sequence):
    # map each nucelotide in the string as a number 
    mapping = {"A": 0, "C": 1, "G": 2, "T": 3, "U": 3}

    one_hot_encoded = []

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

# usage example 

dna='ATTTACGGATTGCTGA'
#calling onehote function
oneHotEncodedDna= onehote(dna)
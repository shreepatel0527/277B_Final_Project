import numpy as np 

# this py file one hot encodes a string of RNA sequence and returns a (len, 4) array

def onehote(sequence):
    # map each nucelotide in the string as a number 
    mapping = {"A": 0, "C": 1, "G": 2, "T": 3, "U": 3}
    seq2 = [mapping[i] for i in sequence]
    return np.eye(4)[seq2]

# usage example 

dna='ATTTACGGATTGCTGA'
#calling onehote function
oneHotEncodedDna= onehote(dna)
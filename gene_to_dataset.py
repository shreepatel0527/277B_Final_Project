# this script pre-processes all genetic data before sending to modeling

import os

os.system("pip install biopython")
os.system("pip install SeqIO")

from Bio import SeqIO
import pandas as pd
from collections import Counter
from onehot import onehote

# Directory containing the dataset
base_dir = "./dataset"

# Function to parse a single .fna file and extract sequence
def parse_fna(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(str(record.seq))
    return sequences

def get_header_as_list(file_path):
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith(">"):  # Check if the line is a header
                return line.strip().split(" ")  # Strip newline and split by space
    return []

# Function to compute k-mer frequencies
def compute_kmer_frequencies(sequence, k=3):
    kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    kmer_counts = Counter(kmers)
    total_kmers = sum(kmer_counts.values())
    # Normalize counts
    kmer_frequencies = {f"kmer_{k}_{key}": val / total_kmers for key, val in kmer_counts.items()}
    return kmer_frequencies

# Function to compute GC content
def compute_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return gc_count / len(sequence) if len(sequence) > 0 else 0

# Function to compute AT/GC ratio
def compute_at_gc_ratio(sequence):
    at_count = sequence.count("A") + sequence.count("T")
    gc_count = sequence.count("G") + sequence.count("C")
    return at_count / gc_count if gc_count > 0 else 0

# Process all files in the dataset directory
data = []

for root, dirs, files in os.walk(base_dir):
    for file_name in files:
        if file_name.endswith(".fna"):
            # Determine folder name (e.g., 'regen' or 'non-regen')
            folder_name = os.path.basename(root)
            regen_value = 1 if folder_name.lower() == "regen" else 0  # regen: 1, non-regen: 0

            # Parse file
            gene_name = file_name.replace("axolotl_", "").replace("_.fna", "")
            file_path = os.path.join(root, file_name)
            sequences = parse_fna(file_path)

            first_line = get_header_as_list(file_path)

            organism = first_line[2].split("=")[1] + " " + first_line[3].strip("]")
            gene_id = first_line[4].split("=")[1].strip("]")
            chromosome = first_line[5].split("=")[1].strip("]")

            for seq in sequences:
                data.append({"gene_name": gene_name, "sequence": seq, "organism": organism, "gene_id": gene_id,"chromosome": chromosome, "regen": regen_value})

# Convert to DataFrame
df = pd.DataFrame(data)
print(f"Processed {len(df)} sequences.")
print(df.head())

# Generate features for each sequence
features = []
for _, row in df.iterrows():
    sequence = row['sequence']
    feature_row = {
        "gene_name": row['gene_name'],
        "sequence_length": len(sequence),
        "gc_content": compute_gc_content(sequence),
        "at_gc_ratio": compute_at_gc_ratio(sequence),
    }
    # Add k-mer frequencies (e.g., k=3)
    feature_row.update(compute_kmer_frequencies(sequence, k=3))
    features.append(feature_row)

# Convert features to DataFrame
features_df = pd.DataFrame(features)

# Fill missing k-mers with zeros
features_df.fillna(0, inplace=True)

print(features_df.head())

# Save features to CSV for modeling
features_df.to_csv("gene_features.csv", index=False)

# now, one hot encode the sequences 
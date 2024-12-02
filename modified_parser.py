# Organism OHE
def one_hot_encode_organism(df, organism_col):
    """
    One-hot encodes organisms into 'ax' and 'ze' columns.
    - 'ax' = 1 if organism is 'Ambystoma mexicanum', else 0
    - 'ze' = 1 if organism is 'Danio rerio', else 0
    
    Args:
        df (pd.DataFrame): The dataframe containing the organism column.
        organism_col (str): The name of the column with organism data.
        
    Returns:
        pd.DataFrame: A new dataframe with 'ax' and 'ze' columns added.
    """
    df = df.copy()
    df['ax'] = df[organism_col].apply(lambda x: 1 if x == 'Ambystoma mexicanum' else 0)
    df['ze'] = df[organism_col].apply(lambda x: 1 if x == 'Danio rerio' else 0)
    return df



import os
from Bio import SeqIO
import pandas as pd

# Directory containing the dataset
# base_dir = base + "dataset/dataset"

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

# Process all files in the dataset directory
data = []

for root, dirs, files in os.walk(base_dir):
    for file_name in files:
        if file_name.startswith(("axolotl", "zebrafish")) and file_name.endswith(".fna"):  # add "zebrafish" to include 
            # Determine folder name (e.g., 'regen' or 'non-regen')
            folder_name = os.path.basename(root)
            regen_value = 1 if folder_name.lower() == "regen" else 0  # regen: 1, non-regen: 0

            # Parse file
            gene_name = file_name.replace("axolotl_", "").replace("zebrafish_", "").replace("_.fna", "")
            file_path = os.path.join(root, file_name)
            sequences = parse_fna(file_path)

            first_line = get_header_as_list(file_path)

            organism = first_line[2].split("=")[1] + " " + first_line[3].strip("]")
            gene_id = first_line[4].split("=")[1].strip("]")
            chromosome = first_line[5].split("=")[1].strip("]")

            for seq in sequences:
                data.append({"gene_name": gene_name, "sequence": seq, "organism": organism, "gene_id": gene_id, "chromosome": chromosome, "regen": regen_value})
        # non-regen part 

# Convert to DataFrame
df = pd.DataFrame(data)

df_organism_OHE = one_hot_encode_organism(df, 'organism')

print(f"Processed {len(df)} sequences.")
print(df.head())

# Save as a CSV for feature engineering
df.to_csv("processed_genes.csv", index=False)
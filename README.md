# Predicting Gene Sequence Regenerative Contributions 

This repository contains machine learning algorithms for predicting regenerative features from gene sequences in vertebrates. This is the final project for CHEM 277B.

## Background

Regeneration is the process by which wounds, tissues, and organs heal themselves within organisms. Often, this can be replacing destroyed cells or restoring entire limbs. Regeneration has been studied extensively because it is a complex process involving many features. An important feature of the genes associated with regeneration is the corresponding interaction network. Understanding how these genes interact with each other can be complicated and difficult, but interaction networks hold crucial information to figuring out the mechanisms of regenerative systems.

With the increasing use of technology in science, researchers have turned to computer-aided methods, such as machine learning, to understand this process. The existing genomic data is rich due to advancements in sequencing technology, forming large banks of data waiting to be mined. 
This project aims to better understand and classify genes related to regeneration using machine learning methods. More specifically, the work focused on classifying coding regions of vertebrate species using neural networks. 

## Repository Contents

### `dataset`

This folder contains the FASTA files downloaded from the NCBI's gene database. This folder is further divided into `regen` and `non-regen` folders so the data processing pipeline can accurately encode genes from their originating folders. The genes used in the work come from the axolotl, zebrafish, and Norwegian rat. 

### `deprecated_txt_csv`

This folder contains `.csv` files and `.txt` files that are no longer in use becaues the data processing pipeline evolved to add more features. The `.csv` files contain genes that were processed prior to modeling. The `.txt` files were used with the NCBI's command line tool to download a large number of genes at once. They contain gene ID's of the genes that were downloaded. 

### `deprecated_coding_files`

This folder contains old Jupyter notebooks from when the model and the data processing pipeline were in the early stages of development. These notebooks are not fully developed and contain parsing functions, PCA on old models, early gridsearch implementations, and early preliminary CNN's. The longer notebooks contain an encoder / decoder developed for use on Kaggle, which failed due to memory limits. The notebooks that start with `sp` summarize the methods tried in other notebooks, as those notebooks were used to compile and compare the work done previously. 

(here, describe the other files in the root directory)

## Results 

Several models were developed to classify genes as regenerative or non-regenerative, leveraging different neural network architectures and data preprocessing techniques. Each model was built with a CNN backbone, with variations in the long-term interaction components, such as LSTM and attention layers, along with different training datasets.

Through this work, it was observed that simpler models like Model 1, which used k-mer counts, may potentially overfit due to the removal of positional information and limited data size. K-Fold cross-validation confirmed that this model was not generalizable across different folds.

Model 2 retained positional sequence features by using one-hot encoded and tokenized sequences with an attention layer. This approach achieved the highest accuracy and F1 score but at a significant computational cost, making it less scalable for larger datasets.

Model 3 introduced FFT to capture long-term interactions with a mathematical conversion, improving run time significantly. However, the accuracy suffered, implying a trade-off between computational efficiency and predictive performance.

## Biological Implications

K-mers, the key feature used in Model 1, are oligonucleotides composed of k nucleotides. This feature captures recurring patterns in DNA sequences, such as the 9-base-pair nonamer sequence that serves as the binding site for DnaA in E. coli. For this project, 3-mers were used, corresponding to codons that directly code for amino acids. Analyzing 3-mers is biologically significant because they determine the amino acid sequence of proteins, influencing structure and function.

The approach to tokenize DNA sequences involved identifying the AUG start codon and translating until one of the terminating codons (UAA, UAG, UGA) appears. This method helps predict molecular characteristics of regenerative proteins. For example, regenerative sequences are more likely to contain codons for amino acids such as leucine (branched functional groups) and threonine or asparagine (polar functional groups).

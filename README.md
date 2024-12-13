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

## Results and Implications

(include after modeling work is complete)



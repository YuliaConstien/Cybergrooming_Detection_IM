# Cyber Grooming Detection in Online Chats
Repository for the Individual Research Module at the University of Potsdam on cyber grooming detection in online Chats.
The goal of the project is to classify online chats into predatory and non-predatory using the multilingual model XMLRoBERTa. The training and evaluation of the model were conducted in 3 different settings to asses its ability to distinguish between cyber grooming and non-cyber grooming conversations in English, German, French and Dutch. The model was evaluated additionally using the CheckList framework to test some of its specific capabilities. The dataset used in the project is the publicly available PAN12 dataset, provided by the PAN Lab at the 2012 CLEF conference for a shared task on sexual predator identification.

## Structure of Repository

### Data

Contains all datasets as follwos: 
- DutchData: contains train, validation and test sets in Dutch
- EnglishData: contains train, validation and test sets in English
- FrenchData: contains train, validation and test sets in French
- Germandata: contains train, validation and test sets in German
- JsonData: contains the original train and test sets cleaned, normalized and tranlsated into 3 languages in json format
- VTPAN_train_IDs.txt: text file with the training conversations ids used in the final training set 
- VTPAN_test_IDs.txt: text file with the test conversations ids used in the final test set

## src

Contains all computaional as follows: 
- CrossLing:
- MonoLing:
- MultiLing:
-

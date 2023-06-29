# Cyber Grooming Detection in Online Chats
Repository for the Individual Research Module at the University of Potsdam on cyber grooming detection in online Chats.
The goal of the project is to classify online chats into predatory and non-predatory using the multilingual model XMLRoBERTa. The training and evaluation of the model were conducted in 3 different settings to asses its ability to distinguish between cyber grooming and non-cyber grooming conversations in English, German, French and Dutch. The model was evaluated additionally using the CheckList framework to test some of its specific capabilities. The dataset used in the project is the publicly available PAN12 dataset, provided by the PAN Lab at the 2012 CLEF conference for a shared task on sexual predator identification.

## Structure of Repository

### Data

Contains all datasets as follwos: 
- **DutchData**: contains train, validation and test sets in Dutch
- EnglishData: contains train, validation and test sets in English
- FrenchData: contains train, validation and test sets in French
- Germandata: contains train, validation and test sets in German
- JsonData: contains the original train and test sets cleaned, normalized and tranlsated into 3 languages in json format
- VTPAN_train_IDs.txt: text file with the training conversations ids used in the final training set 
- VTPAN_test_IDs.txt: text file with the test conversations ids used in the final test set

### src

Contains all computaional as follows: 
- CrossLing: code for training and evaluating the model for German, French and Dutch in the cross-lingual setup
- MonoLing: code for training and evaluating the model for English, German, French and Dutch in the monolingual setup
- MultiLing: code for training and evaluating the model for English, German, French and Dutch in the multilingual setup
- CGD_TranslatedData_preporcessing_json.ipynb: code for creating the final training and test sets i German, French and Dutch
- CGD_dataset_preprocessing.ipynb:  code for data preprocessing steps
- NaiveBayes.py: code fo the baseline model

## Reproducing Results

Install all necessary packages with requirements.txt
'''
$ pip install requirements.txt
'''
Run the jupyter notebook for each language in the CrossLing folder to reproduce the experiments and results for this setting

Run the jupyter notebook for each language in the MonoLing folder to reproduce the experiments and results for this setting 

Follow the steps in xmlRoberta_all_Lang.ipynb in the MultiLing folder to reproduce the experiments and results for this setting 

Follow the steps in CGD_dataset_preprocessing.ipynb to reproduce the preprocessing of the dataset. 

Follow the steps in CGD_TranslatedData_preporcessing_json.ipynb to create the final datasets in all 4 languages in csv format 

To download XMLRoBERTa trained in the multilingual setup from the Huggingface Hub use:

from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Constien/xmlRoberta_all_lang")

model = AutoModelForSequenceClassification.from_pretrained("Constien/xmlRoberta_all_lang")


Reproduce the Naive Bayes by running: 

$ python NaiveBayes.py

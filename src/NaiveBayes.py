import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

from sklearn.naive_bayes import  MultinomialNB
from sklearn.naive_bayes import BernoulliNB

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# change paths
trainJSON = "/home/Yulia/Schreibtisch/Studenten/Yulia Com/data/train-all.json"
testJSON = "/home/Yulia/Schreibtisch/Studenten/Yulia Com/data/test-all.json"

def getData(inJSON):

    with open(inJSON, 'r') as f:
      data = json.load(f)

    imdbTrainTexts = []
    imdbTrainLabels = []
    for conversation in (data['conversations']):
        conversationText = list(map(lambda x: x["normText"], conversation["messages"]))
        fullText = " ".join(conversationText)
        imdbTrainTexts.append(fullText)
        imdbTrainLabels.append(conversation["isCybergrooming"])
    return imdbTrainTexts,imdbTrainLabels

imdbTrainTexts,imdbTrainLabels = getData(trainJSON)
imdbTestTexts,imdbTestLabels = getData(testJSON)


vectorizer = CountVectorizer(max_features=1000)

label_encoder = LabelEncoder()

train_x = vectorizer.fit_transform(imdbTrainTexts)
train_y = label_encoder.fit_transform(imdbTrainLabels)

test_x = vectorizer.transform(imdbTestTexts)
test_y = label_encoder.transform(imdbTestLabels)


#1.) Train Naive-Bayes with all features
bayes = MultinomialNB()
bayes.fit(train_x, train_y)
pred = bayes.predict(test_x)
print(accuracy_score(pred, test_y))
print(confusion_matrix(test_y, pred))

#2.) Perform frature selection in order to identify the most relevant features

from sklearn.feature_selection import chi2
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectKBest

selector = SelectKBest(score_func=mutual_info_classif, k=50)
fit = selector.fit(train_x, train_y)

vocab = vectorizer.vocabulary_
inv_map = {v: k for k, v in vocab.items()}
for value in selector.get_support(indices=True):
    print(inv_map.get(value))
    #print(selector.scores_[value])


#3.) Reduce to selected features and train again
trainX_transformed = selector.transform(train_x)
testX_transformed = selector.transform(test_x)


bayes = MultinomialNB()
bayes.fit(trainX_transformed, train_y)
pred = bayes.predict(testX_transformed)
print(accuracy_score(pred, test_y))
print(confusion_matrix(test_y, pred))



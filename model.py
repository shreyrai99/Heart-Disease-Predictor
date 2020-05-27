import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
heart = pd.read_csv('heart.csv')

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(heart.loc[:,heart.columns != 'target'], heart['target'], stratify=heart['target'], random_state=66)

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(random_state=42)
mlp.fit(X_train, y_train)

#print("Accuracy on training set: {:.2f}".format(mlp.score(X_train, y_train)))
#print("Accuracy on test set: {:.2f}".format(mlp.score(X_test, y_test)))


pickle.dump(mlp, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

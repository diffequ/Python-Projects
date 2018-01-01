# P5-ML1 - Machine Learning practice with Python
# B.KORYAN - Dec 31 2017 @ Fredericton | web : http://koryan.ca
# Citation : Special thanks to Dr.Jason Browlee for writing this article at this link below
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
#------------------------------------------------------------------------------
# Description : The code below basically imports the data at the given URL
# then divides data into two parts as training and validation dataset.Then
# the imported data is classified using Linear Discriminant Analysis(LDA) then
# the classification result is printed as 'msg' after 10-fold cross-validation
#--------------------------------------------------------------------------------

import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

array = dataset.values
x = array[:,0:4]
y = array[:,4]
valid_size = 0.2
seed = 7
scoring = 'accuracy'
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(x, y, test_size=valid_size, random_state=seed)


# Spot Check Algorithms
models = []
models.append(('LDA',LinearDiscriminantAnalysis()))
results = []
names = []


# Classify and print results:
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

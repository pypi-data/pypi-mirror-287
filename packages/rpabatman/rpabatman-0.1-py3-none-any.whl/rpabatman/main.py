def p1():
    code = '''
import numpy as np
import pandas as pd

data = pd.read_csv('lab1.csv')
features = np.array(data)[:,:-1]
target = np.array(data)[:,-1]

for i, val in enumerate(target):
    if val == 'yes':
        specific_h = features[i].copy()
        break

print(specific_h)

for i, val in enumerate(features):
    if target[i] == 'yes':
        for x in range(len(specific_h)):
            if val[x] != specific_h[x]:
                specific_h[x] = '?'
                
print(specific_h)
    '''
    print(code)


def p2():
    code = '''
import numpy as np
import pandas as pd

data = pd.read_csv('lab1.csv')
features = np.array(data)[:,:-1]
target = np.array(data)[:,-1]

specific_h = features[0].copy()
print("initialization of specific_h and general_h")
print(specific_h)

general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
print(general_h)

for i, h in enumerate(features):
    if target[i] == "yes":
        for x in range(len(specific_h)):
            if h[x] != specific_h[x]:
                specific_h[x] = '?'
                general_h[x][x] = '?'
    if target[i] == "no":
        for x in range(len(specific_h)):
            if h[x] != specific_h[x]:
                general_h[x][x] = specific_h[x]
            else:
                general_h[x][x] = '?'
                
    print(specific_h, "\\n")
    print(general_h, "\\n")

indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
for i in indices:
    general_h.remove(['?', '?', '?', '?', '?', '?'])

print("\\nfinal specific_h:", specific_h, sep="\\n")
print("final general_h:", general_h, sep="\\n")
    '''
    print(code)


def p3():
    code = '''
import pandas as pd
from collections import Counter
import math

tennis = pd.read_csv('tennis.csv')
print("\\n given play tennis dataset:\\n\\n", tennis)

def entropy(alist):
    c = Counter(x for x in alist)
    instances = len(alist)
    prob = [x / instances for x in c.values()]
    return sum([-p * math.log(p, 2) for p in prob])

def information_gain(d, split, target):
    splitting = d.groupby(split)
    n = len(d.index)
    agent = splitting.agg({target: [entropy, lambda x: len(x)/n]})[target]
    agent.columns = ['entropy', 'observations']
    newentropy = sum(agent['entropy'] * agent['observations'])
    oldentropy = entropy(d[target])
    return oldentropy - newentropy

def id3(sub, target, a):
    count = Counter(x for x in sub[target])  # class of YES / NO
    if len(count) == 1:
        return next(iter(count))  # next i/p dataset
    else:
        gain = [information_gain(sub, attr, target) for attr in a]
        print("\\n gain=", gain)
        maximum = gain.index(max(gain))
        best = a[maximum]
        print("\\nbest attribute=", best)
        tree = {best: {}}
        remaining = [i for i in a if i != best]

        for val, subset in sub.groupby(best):
            subtree = id3(subset, target, remaining)
            tree[best][val] = subtree
            
        return tree

names = list(tennis.columns)
print("\\nlist of attributes:", names)
names.remove("PlayTennis")
print("\\npredicting attributes:", names)

tree = id3(tennis, 'PlayTennis', names)
print("\\n\\n the resultant decision tree is:\\n")
print(tree)
    '''
    print(code)


def p4():
    code = '''
import numpy as np

x = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

x = x / np.amax(x, axis=0)
y = y / 100

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivatives_sigmoid(x):
    return x * (1 - x)

epoch = 7000
lr = 0.1
inputlayer_neurons = 2
hiddenlayer_neurons = 3
output_neurons = 1

wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))
bh = np.random.uniform(size=(1, hiddenlayer_neurons))
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

for i in range(epoch):
    hinp1 = np.dot(x, wh)
    hinp = hinp1 + bh
    hlayer_act = sigmoid(hinp)
    outinp1 = np.dot(hlayer_act, wout)
    outinp = outinp1 + bout
    output = sigmoid(outinp)
    
    EO = y - output
    outgrad = derivatives_sigmoid(output)
    d_output = EO * outgrad
    EH = d_output.dot(wout.T)
    hiddengrad = derivatives_sigmoid(hlayer_act)
    d_hiddenlayer = EH * hiddengrad
    wout += hlayer_act.T.dot(d_output) * lr
    
print("Input:\\n" + str(x))
print("Actual output: \\n" + str(y))
print("Predicted output:\\n", output)
    '''
    print(code)


def p5():
    code = '''
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score

data = pd.read_csv('textdata12.csv', names=['message', 'label'])
print('the dataset is', data)
print('the dimensions of the dataset', data.shape)

data['labelnum'] = data.label.map({'pos': 1, 'neg': 0})
x = data.message
y = data.labelnum
print(x)
print(y)

vectorizer = TfidfVectorizer()
data = vectorizer.fit_transform(x)
print("\\n the feature of dataset:\\n")
df = pd.DataFrame(data.toarray(), columns=vectorizer.get_feature_names_out())
df.head()

print("\\n train test split")
xtrain, xtest, ytrain, ytest = train_test_split(data, y, test_size=0.3, random_state=42)
print("\\n the total number of training data:", ytrain.shape)
print("\\n the total number of test data:", ytest.shape)

clf = MultinomialNB().fit(xtrain, ytrain)
predict = clf.predict(xtest)
predicted = clf.predict(xtest)

print("\\n accuracy of the classifier is", accuracy_score(ytest, predicted))
print("\\n confusion matrix is\\n", confusion_matrix(ytest, predicted))
print("\\n classification report is\\n", classification_report(ytest, predicted))
print("\\n the value of precision is\\n", precision_score(ytest, predicted))
print("\\n the value of recall is\\n", recall_score(ytest, predicted))
    '''
    print(code)


def p6():
    code = '''
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

col = ['Age', 'Gender', 'Familylist', 'Diet', 'LifeStyle', 'Cholesterol', 'heartDisease']
data = pd.read_csv('lab6.csv', names=col)
print(data)

encoder = LabelEncoder()
for i in range(len(col)):
    data.iloc[:, i] = encoder.fit_transform(data.iloc[:, i])

X = data.iloc[:, 0:6]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = GaussianNB()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print('confusion matrix', confusion_matrix(y_test, y_pred))
    '''
    print(code)


def p7():
    code = '''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans

data = pd.read_csv('lab7.csv')
print('Input Data and Shape')
print(data.shape)
data.head()

f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1, f2)))
print("X", X)
print("Graph for whole dataset")
plt.scatter(f1, f2, c='black', s=15)
plt.show()

kmeans = KMeans(10, random_state=42)
labels = kmeans.fit(X).predict(X)
print("labels ", labels)
centroids = kmeans.cluster_centers_
print("Centroids ", centroids)

plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
print("Graph using Kmeans Algorithm ")
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='#050505')
plt.show()

gmm = GaussianMixture(n_components=3).fit(X)
labels = gmm.predict(X)
probs = gmm.predict_proba(X)
size = 10 * probs.max(1) ** 3

print("Graph using Em algorithm")
plt.scatter(X[:, 0], X[:, 1], c=labels, s=size, cmap='viridis')
plt.show()
    '''
    print(code)


def p9():
    code = '''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

tou = 1
data = pd.read_csv("tips.csv")
X_train = np.array(data.total_bill)
print(X_train)
X_train = X_train[:, np.newaxis]
print(len(X_train))
y_train = np.array(data.tip)

X_test = np.array([i / 10 for i in range(500)])
X_test = X_test[:, np.newaxis]
y_test = []

count = 0
for r in range(len(X_test)):
    wts = np.exp(-np.sum((X_train - X_test[r]) ** 2, axis=1) / (2 * tou ** 2))
    W = np.diag(wts)
    factor1 = np.linalg.inv(X_train.T.dot(W).dot(X_train))  # factor = XT.W.X
    parameters = factor1.dot(X_train.T).dot(W).dot(y_train)
    prediction = X_test[r].dot(parameters)
    y_test.append(prediction)
    count += 1

print(len(y_test))
y_test = np.array(y_test)

plt.plot(X_train.squeeze(), y_train, 'o')
plt.plot(X_test.squeeze(), y_test, 'o')
plt.show()
    '''
    print(code)


def p10():
    code = '''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

datasets = pd.read_csv('lab10.csv')
X = datasets.iloc[:, [2, 3]].values
Y = datasets.iloc[:, 4].values

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.25, random_state=0)

sc_X = StandardScaler()
X_Train = sc_X.fit_transform(X_Train)
X_Test = sc_X.transform(X_Test)

classifier = SVC(kernel='linear', random_state=0)
classifier.fit(X_Train, Y_Train)
Y_Pred = classifier.predict(X_Test)

from sklearn import metrics
print("Accuracy score ", metrics.accuracy_score(Y_Test, Y_Pred))

plt.scatter(X_Train[:, 0], X_Train[:, 1], c=Y_Train)
plt.title('Support Vector Machine (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')

w = classifier.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-2.5, 2.5)
yy = a * xx - (classifier.intercept_[0]) / w[1]
plt.plot(xx, yy)
plt.show()

plt.scatter(X_Test[:, 0], X_Test[:, 1], c=Y_Test)
plt.title('Support Vector Machine (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.plot(xx, yy)
plt.show()
    '''
    print(code)

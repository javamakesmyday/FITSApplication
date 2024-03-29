# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

print('======SHAPE======')
# shape
print(dataset.shape)

print('======HEAD======')
# head
print(dataset.head(20))

print('======DESCRIPTIONS======')
# descriptions
print(dataset.describe())

print('======CLASS DISTRIBUTION======')
# class distribution
print(dataset.groupby('class').size())

print('======BOX AND WHISKER PLOTS======')
# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

print('======HISTOGRAMS======')
# histograms
dataset.hist()
plt.show()

print('======SCATTER PLOT MATRIX======')
# scatter plot matrix
scatter_matrix(dataset)
plt.show()



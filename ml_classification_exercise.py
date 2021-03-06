# The Iris dataset is referred to as a “toy dataset” because it has only 150 samples and four features. 
# The dataset describes 50 samples for each of three Iris flower species—Iris setosa, Iris versicolor and Iris 
# virginica. Each sample’s features are the sepal length, sepal width, petal 
# length and petal width, all measured in centimeters. The sepals are the larger outer parts of each flower 
# that protect the smaller inside petals before the flower buds bloom.

#EXERCISE
# load the iris dataset and use classification
# to see if the expected and predicted species
# match up

# display the shape of the data, target and target_names

# display the first 10 predicted and expected results using
# the species names not the number (using target_names)

# display the values that the model got wrong

# visualize the data using the confusion matrix

import pandas as pd

from sklearn.datasets import load_iris
iris = load_iris()


from sklearn.model_selection import train_test_split

data_train, data_test, target_train,target_test   =train_test_split(
iris.data, iris.target, random_state=11
)




from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
# Knn=LogisticRegression(C=1,solver='liblinear',max_iter=5000,class_weight='balanced',penalty='l2')
Knn=KNeighborsClassifier()




# from sklearn.linear_model import LogisticRegression
# Knn=LogisticRegression()




Knn.fit(X=data_train, y= target_train)

predicted=Knn.predict(X=data_test)

expected= target_test

print(predicted[:20])
print(expected[:20])

wrong= [(p,e) for (p,e) in zip(predicted,expected) if p !=e ]

print(len(wrong))

print(format(Knn.score(data_test, target_test), ".2%"))


from sklearn.metrics import confusion_matrix
confusion= confusion_matrix(y_true=expected, y_pred=predicted)

print(confusion)


import seaborn as sns
import matplotlib.pyplot as plt2

confusion_df= pd.DataFrame(confusion,columns=['setosa', 'versicolor' ,'virginica'],index=['setosa', 'versicolor' ,'virginica'])



print(confusion_df)


figure=plt.figure(figsize=(7,6))
axes=sns.heatmap(confusion_df,annot=True,cmap=plt.cm.nipy_spectral_r)


plt.show()







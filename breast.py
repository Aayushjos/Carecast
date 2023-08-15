import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
import seaborn as sb
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score ,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import mean_squared_error

df= pd.read_csv("breast-cancer.csv")
# print(df.info())
# print(df.shape)
print(df.columns)
# df.hist()
# plt.show()
# corrmat = df.corr()
# top_corr_features = corrmat.index
# plt.figure(figsize=(20,20))
# g = sb.heatmap(df[top_corr_features].corr(),annot=True)
# plt.show()
X =df.drop(['id','diagnosis','texture_mean','smoothness_mean','symmetry_mean', 'fractal_dimension_mean','compactness_mean','texture_se','smoothness_se','symmetry_se',
       'fractal_dimension_se','compactness_se','texture_worst','symmetry_worst', 'fractal_dimension_worst','compactness_worst','smoothness_worst'],axis=1)
Y = df['diagnosis']
df['diagnosis'].replace(['B', 'M'], [0, 1], inplace=True)
# print(Y)
X_train , X_test ,Y_train , Y_test = train_test_split(X,Y,random_state=40,test_size=0.20)
# print("The shape of X_train :"+ str(X_train.shape))
# print("The shape of Y_train :"+ str(Y_train.shape))
# print("The shape of X_test :"+ str(X_test.shape))
# print("The shape of Y_test :"+ str(Y_test.shape))
Logreg = LogisticRegression(random_state=0,max_iter=500)
Logreg.fit(X_train,Y_train)
Y_pred = Logreg.predict(X_test)
acc = accuracy_score(Y_test,Y_pred)
print("The accuracy score is:"+ str(acc))
f1 = f1_score(Y_test,Y_pred)
print("The f1_score is :"+ str(f1))
cf = confusion_matrix(Y_test,Y_pred)
print(cf)
# predicted = Logreg.predict(X_test)
# d = pd.DataFrame({'Actual': Y_test, 'Predicted': predicted})
# graph = d.head(100)
# graph.plot(kind='bar')
# plt.show()


# breast_cancer_model.py

import pickle

def load_model():
    return pickle.load(open('breast.pickle', 'rb'))


model = load_model()

def predict_breast_cancer(radius_mean, perimeter_mean, area_mean, concavity_mean, concave_points_mean,
                          radius_se, perimeter_se, area_se, concavity_se, concave_points_se,
                          radius_worst, perimeter_worst, area_worst, concavity_worst, concave_points_worst):
    x = np.array([[radius_mean, perimeter_mean, area_mean, concavity_mean, concave_points_mean,
                   radius_se, perimeter_se, area_se, concavity_se, concave_points_se,
                   radius_worst, perimeter_worst, area_worst, concavity_worst, concave_points_worst]])
    prediction = model.predict(x)
    return "Malignant" if prediction[0] == 1 else "Benign"



     

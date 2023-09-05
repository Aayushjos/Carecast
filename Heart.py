import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix , f1_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import seaborn as sb
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
import pickle
import json


df = pd.read_csv("heart.csv")
print(df.columns)
X = df.drop(['target','slope','ca','exang','thal','fbs','restecg'],axis =1)
Y = df['target']
# df.hist()
# plt.show()
corrmat= df.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
g = sb.heatmap(df[top_corr_features].corr(),annot=True,)
plt.show()
X_train ,X_test , Y_train ,Y_test = train_test_split(X,Y,random_state=0,test_size=0.25)
model = RandomForestClassifier(n_estimators=10,max_depth=7)
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
acc =accuracy_score(Y_test,Y_pred)
print("The accuracy score is " +str(acc))
cf = confusion_matrix(Y_test,Y_pred)
f1  =f1_score(Y_test,Y_pred)
# a = df['age'][:1000]
# b = df['target'][:1000]
# plt.scatter(x =a,y= b,marker="*")
# plt.show()
print(cf)
print(f1)
# sb.set_style('whitegrid')
# sb.countplot(x='target',data=df)
# plt.show()

scores = cross_val_score(model,X,Y,cv =10)
print(scores)
cv =ShuffleSplit(n_splits=4,test_size=0.2,random_state=0)
print(cross_val_score(model,X,Y,cv=cv))
predicted = model.predict(X_test)
d = pd.DataFrame({'Actual':Y_test,"Predicted" :predicted})
graph = d.head(30)
graph.plot(kind='bar')
plt.show()

def load_model():
    return pickle.load(open('Heart.pickle', 'rb'))

def predict_heart_disease(age,sex,cp,trestbps,chol,thalach,oldpeak):
    x = np.zeros(len(X.columns))
    x[0]= age
    x[1]= sex
    x[2]= cp
    x[3]= trestbps
    x[4]= chol
    x[5]= thalach
    x[6]= oldpeak
    return model.predict([x])
predict =predict_heart_disease(54,1,0,120,188,113,1.4)
if predict  ==[1]:
   print("You have a heart disease , take care !!")
else:
    print("Great!!, you are healthy ,keep going.")
    # Saving the model
import joblib
joblib.dump(model,'Heart_disease.pickle')

    

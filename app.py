import flask
from flask import render_template, Flask, request, redirect, url_for
import joblib
import pandas as pd
import numpy as np

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}

app = Flask(__name__)

# Breast Cancer Prediction
def load_breast_cancer_model():
    return joblib.load('breast.pickle')

def perform_breast_cancer_prediction(radius_mean, perimeter_mean, area_mean, concavity_mean, concave_points_mean,
                                     radius_se, perimeter_se, area_se, concavity_se, concave_points_se,
                                     radius_worst, perimeter_worst, area_worst, concavity_worst, concave_points_worst):
    model = load_breast_cancer_model()
    x = [[radius_mean, perimeter_mean, area_mean, concavity_mean, concave_points_mean,
          radius_se, perimeter_se, area_se, concavity_se, concave_points_se,
          radius_worst, perimeter_worst, area_worst, concavity_worst, concave_points_worst]]
    prediction = model.predict(x)
    return prediction[0]

@app.route('/breastcancer',methods = ['GET'])
def breast_cancer_home():
    return render_template('breastcancer.html')

@app.route('/predict', methods=['GET','POST'])
def predict_breast_cancer():
    if request.method == 'POST':
        radius_mean = float(request.form['radius_mean'])
        perimeter_mean = float(request.form['perimeter_mean'])
        area_mean = float(request.form['area_mean'])
        concavity_mean = float(request.form['concavity_mean'])
        concave_points_mean = float(request.form['concave_points_mean'])
        radius_se = float(request.form['radius_se'])
        perimeter_se = float(request.form['perimeter_se'])
        area_se = float(request.form['area_se'])
        concavity_se = float(request.form['concavity_se'])
        concave_points_se = float(request.form['concave_points_se'])
        radius_worst = float(request.form['radius_worst'])
        perimeter_worst = float(request.form['perimeter_worst'])
        area_worst = float(request.form['area_worst'])
        concavity_worst = float(request.form['concavity_worst'])
        concave_points_worst = float(request.form['concave_points_worst'])

        result = perform_breast_cancer_prediction(radius_mean, perimeter_mean, area_mean, concavity_mean, concave_points_mean,
                                                  radius_se, perimeter_se, area_se, concavity_se, concave_points_se,
                                                  radius_worst, perimeter_worst, area_worst, concavity_worst, concave_points_worst)

        if result == 0:
            prediction = "Benign"
        else:
            prediction = "Malignant"

        return render_template('result.html', prediction=prediction)
    else:
        return render_template('breastcancer.html')

# Rest of the code for Diabetes and Kidney Prediction (as you provided earlier)





# Diabetes Prediction
def load_diabetes_model():
    return joblib.load('diab.pickle')

def predict_diabetes(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    model = load_diabetes_model()
    x = [[Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
    prediction = model.predict(x)
    return prediction[0]

@app.route('/diabetes', methods =['GET'])
def diabetes_home():
    return render_template('diabetes.html')

@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes_route():
    Glucose = float(request.form['Glucose'])
    BloodPressure = float(request.form['BloodPressure'])
    SkinThickness = float(request.form['SkinThickness'])
    Insulin = float(request.form['Insulin'])
    BMI = float(request.form['BMI'])
    DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
    Age = float(request.form['Age'])

    result = predict_diabetes(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

    if result == 0:
        prediction = "You are not Diabetic."
    else:
        prediction = "You are Diabetic. Please consult a doctor."

    return render_template('result1.html', prediction=prediction)

# Ayurveda Prediction (Kidney)



# Load and preprocess the data
data = pd.read_csv('kidney_disease.csv')
data.classification = data.classification.replace("ckd\t", "ckd")
data['classification'] = data['classification'].replace(['ckd', 'notckd'], [1, 0])
df = data.dropna(axis=0)
dictonary = {
    "rbc": {
        "abnormal": 1,
        "normal": 0,
    },
    "pc": {
        "abnormal": 1,
        "normal": 0,
    },
    "pcc": {
        "present": 1,
        "notpresent": 0,
    },
    "ba": {
        "notpresent": 0,
        "present": 1,
    },
    "htn": {
        "yes": 1,
        "no": 0,
    },
    "dm": {
        "yes": 1,
        "no": 0,
    },
    "cad": {
        "yes": 1,
        "no": 0,
    },
    "appet": {
        "good": 1,
        "poor": 0,
    },
    "pe": {
        "yes": 1,
        "no": 0,
    },
    "ane": {
        "yes": 1,
        "no": 0,
    }
}
df = df.replace(dictonary)
a = df.drop(['classification', 'sg', 'appet', 'rc', 'pcv', 'hemo', 'sod', 'pot', 'ane', 'su', 'cad', 'bp', 'rbc', 'pcc', 'ba','id'], axis=1)
b = df['classification']

# Train the model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.25, random_state=0)
model = LogisticRegression()
model.fit(a_train, b_train)

@app.route('/kidney', methods =['GET'])
def kidney_home():
    return render_template('kidney.html')



@app.route('/predict_kidney', methods=['POST'])
def predict_kidney():
    # Get input data from the form
    age = int(request.form['age'])
    al = float(request.form['al'])
    pc = request.form['pc']
    bgr = int(request.form['bgr'])
    bu = int(request.form['bu'])
    sc = float(request.form['sc'])
    wc = int(request.form['wc'])
    htn = request.form['htn']
    dm = request.form['dm']
    pe = request.form['pe']

    # Preprocess the input data
    a_input = pd.DataFrame({
        'age': [age],
        'al': [al],
        'pc': [pc],
        'bgr': [bgr],
        'bu': [bu],
        'sc': [sc],
        'wc': [wc],
        'htn': [htn],
        'dm': [dm],
        'pe': [pe]
    })

    # Make sure the column names in X_input match those in X_train
    a_input = a_input[a_train.columns]

    # Make the prediction
    prediction = model.predict(a_input)

    # Convert the prediction to a human-readable form
    if prediction[0] == 1:
        result = "Positive (CKD)"
    else:
        result = "Negative (not CKD)"

    return render_template('result2.html', prediction=result)






def load_heart_model():
    return joblib.load('Heart_disease.pickle')

def predict_heart( age ,sex ,cp ,trestbps ,chol ,thalach ,oldpeak):
    model = load_heart_model()
    x = [[ age,sex,cp,trestbps,chol,thalach,oldpeak]]
    prediction = model.predict(x)
    return prediction[0]

@app.route('/heart.html', methods =['GET'])
def heart_home():
    return render_template('heart.html')

@app.route('/predict_heart', methods=['POST'])
def predict_heart_route():
    age = float(request.form['age'])
    sex = float(request.form['sex'])
    cp = float(request.form['cp'])
    trestbps = float(request.form['trestbps'])
    chol = float(request.form['chol'])
    thalach = float(request.form['thalach'])
    oldpeak = float(request.form['oldpeak'])

    result = predict_heart(age, sex, cp, trestbps,chol, thalach, oldpeak)

    if result == 0:
        prediction = "You are Healthy!."
    else:
        prediction = "You have a Heart Disease. Please consult a doctor."

    return render_template('result3.html', prediction=prediction)


































# Ayurveda-related Routes
@app.route('/project.html')
def project():
    return render_template('project.html')

@app.route('/ayu.html')
def ayu():
    return render_template('ayu.html')

@app.route('/ayu.test.html')
def ayu_test():
    return render_template('/ayu.test.html')

@app.route('/result_balanced.html')
def balance():
    return render_template('/result_balanced.html')

@app.route('/result_kapha.html')
def kapha():
    return render_template('/result_kapha.html')

@app.route('/result_pitta_kapha.html')
def pk():
    return render_template('/result_pitta_kapha.html')

@app.route('/result_pitta.html')
def pitta():
    return render_template('/result_pitta.html')

@app.route('/result_vatta.html')
def vata():
    return render_template('/result_vatta.html')

@app.route('/result_vatta_pitta.html')
def vp():
    return render_template('/result_vatta_pitta.html')

@app.route('/result_vatta_kapha.html')
def vk():
    return render_template('/result_vatta_kapha.html')

@app.route('/blogs.html', methods =['GET'])
def blogs():
    return render_template('/blogs.html')

if __name__ == '__main__':
    app.run(debug=True)











    













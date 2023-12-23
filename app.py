import flask
import pandas as pd 
import numpy as np 
from flask import render_template ,Flask, request , redirect , url_for
import joblib

app  = Flask(__name__)
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










    













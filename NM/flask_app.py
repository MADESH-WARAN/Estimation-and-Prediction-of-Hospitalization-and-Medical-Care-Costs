from flask import Flask, render_template, request
import numpy as np
from templates.train_a import *

app = Flask(__name__)

# localhost:5000/ -> home page
@app.route('/')
def home():
    return render_template('index.html')

# i have a model.pkl file that contains the model and the predict function and it returns the prediction

@app.route('/predict', methods=['POST'])
def predict():
    sex= request.form['sex']
    region=request.form['region']
    smoker=request.form['smoker']
    regions=["NorthEast","NorthWest","SouthEast","SouthWest"]
    d={'age': 0,'bmi': 0,'children': 0,'sex_female': 0,'sex_male': 0,'smoker_no': 0,'smoker_yes': 0,'region_northeast': 0,'region_northwest': 0,'region_southeast': 0,'region_southwest': 0}
    d['bmi']=int(request.form['bmi'])
    d['age']=int(request.form['age'])
    d['children']=int(request.form['children'])
    for i in regions:
        if i==region:
            index = regions.index(region)
            d_index=index+7
    keys_list = list(d.keys())
    d[keys_list[d_index]]=1
    if sex=='Male':
        d['sex_male']=1
    else:
        d['sex_female']=1
    if smoker=='Yes':
        d['smoker_yes']=1
    else:
        d['smoker_no']=1
    values_list = list(d.values())
    pred = medical_expense_prediction(values_list)

    return render_template('index.html',value=pred)
if __name__ == "__main__":
    app.run(debug=True)

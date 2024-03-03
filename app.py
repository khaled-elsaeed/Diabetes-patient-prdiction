from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__,static_url_path='/static')

model = joblib.load('Diabetes prediction\diabetes_model.joblib')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    user_input = [float(request.form[feature]) for feature in features]

    input_data = pd.DataFrame([user_input], columns=features)

   

    prediction = predict_diabetes(input_data)
    return render_template('result.html', prediction=prediction)

def predict_diabetes(input_data):
    result = model.predict(input_data)[0] 
    return "High risk of diabetes" if result == 1 else "Low risk of diabetes"

if __name__ == '__main__':
    app.run(debug=True)

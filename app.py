from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('loan_model.pkl')  # Load your trained model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from the form
    gender = 1 if request.form['gender'] == 'Male' else 0
    married = 1 if request.form['married'] == 'Yes' else 0
    dependents = int(request.form['dependents'])
    education = 0 if request.form['education'] == 'Graduate' else 1
    self_employed = 1 if request.form['self_employed'] == 'Yes' else 0
    applicant_income = float(request.form['applicant_income'])
    coapplicant_income = float(request.form['coapplicant_income'])
    loan_amount = float(request.form['loan_amount'])
    loan_term = float(request.form['loan_term'])
    credit_history = float(request.form['credit_history'])
    property_area = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}[request.form['property_area']]

    # Prepare input for prediction
    input_data = np.array([[gender, married, dependents, education, self_employed,
                            applicant_income, coapplicant_income, loan_amount,
                            loan_term, credit_history, property_area]])

    # Predict
    result = model.predict(input_data)[0]
    prediction = "Eligible ✅" if result == 1 else "Not Eligible ❌"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

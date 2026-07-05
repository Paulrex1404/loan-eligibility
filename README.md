Loan Eligibility Predictor

Overview:

The Loan Eligibility Predictor is a Machine Learning web application that predicts whether a loan application is likely to be approved based on applicant details. The model analyzes user inputs such as income, education, employment status, loan amount, credit history, and other relevant factors to provide an instant prediction.

Features:

Predicts loan approval eligibility
User-friendly web interface
Real-time prediction
Data preprocessing before prediction
Machine Learning-based classification model

Tech Stack:

Programming Language: Python
Machine Learning: Scikit-learn
Data Processing: Pandas, NumPy
Frontend: HTML, CSS, JavaScript
Backend: Flask
Model Storage: Pickle

Project Structure:

Loan-Eligibility-Predictor/
│── app.py
│── model.pkl
│── requirements.txt
│── templates/
│     └── index.html
│── static/
│     ├── style.css
│     └── script.js
│── dataset.csv
│── train_model.py
└── README.md

Installation:

Clone the repository
git clone https://github.com/Paulrex1404/Loan-Eligibility-Predictor.git
Navigate to the project folder
cd Loan-Eligibility-Predictor
Install the required packages
pip install -r requirements.txt
Run the application
python app.py
Open your browser and visit:
http://127.0.0.1:5000

Input Parameters:

The model uses the following inputs:

Gender
Marital Status
Dependents
Education
Self Employment
Applicant Income
Co-applicant Income
Loan Amount
Loan Amount Term
Credit History
Property Area

Output:

The application predicts whether the loan application is:

✅ Loan Approved
❌ Loan Not Approved
📈 Machine Learning Workflow
Data Collection
Data Preprocessing
Feature Encoding
Model Training
Model Evaluation
Model Saving
Web Application Deployment

Future Enhancements:

Improve prediction accuracy using advanced ML algorithms
Deploy the application on a cloud platform
Add user authentication
Store prediction history in a database
Enhance the UI for better user experience

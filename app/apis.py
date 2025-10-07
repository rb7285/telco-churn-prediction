from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initializing Flask app
app = Flask(__name__)

# Loading saved model
model = joblib.load("churn_model.pkl")

# Defining prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # JSON input from user
    df = pd.DataFrame([data])  # dict → DataFrame

    # Predicting probability
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return jsonify({
        "prediction": str(prediction),
        "churn_probability": round(float(probability), 3)
    })

if __name__ == '__main__':
    app.run(debug=True)

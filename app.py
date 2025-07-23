# app.py
from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load saved model and preprocessor
model = joblib.load("models/personalised_health_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")
features = joblib.load("models/feature_names.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    recommendations = []

    if request.method == "POST":
        input_data = []
        for feature in features:
            val = float(request.form.get(feature, 0))
            input_data.append(val)

        input_df = pd.DataFrame([input_data], columns=features)
        processed = preprocessor.transform(input_df)
        prediction = model.predict(processed)[0]

        if prediction == "High":
            recommendations = [
                "Consult a healthcare provider immediately.",
                "Maintain a healthy diet.",
                "Exercise regularly.",
                "Monitor your symptoms daily."
            ]
        elif prediction == "Medium":
            recommendations = [
                "Get a regular health checkup.",
                "Maintain a balanced lifestyle.",
                "Avoid smoking or drinking."
            ]
        else:
            recommendations = [
                "Keep up your good lifestyle!",
                "Continue regular physical activity.",
                "Maintain stress-free habits."
            ]

    return render_template("index.html", features=features, prediction=prediction, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
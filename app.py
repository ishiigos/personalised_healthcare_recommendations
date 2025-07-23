from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model components
model = joblib.load("models/personalised_health_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")
feature_names = joblib.load("models/feature_names.pkl")  # List of all input fields expected

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    recommendations = []

    if request.method == "POST":
        try:
            # Collect and typecast input data
            input_data = {}
            for feature in feature_names:
                raw_val = request.form.get(feature)

                if raw_val is None or raw_val == "":
                    input_data[feature] = 0  # or use None/defaults if applicable
                elif raw_val.replace(".", "", 1).isdigit() or raw_val.isdigit():
                    input_data[feature] = float(raw_val)
                else:
                    input_data[feature] = raw_val

            input_df = pd.DataFrame([input_data])

            # Preprocess and predict
            transformed = preprocessor.transform(input_df)
            prediction = model.predict(transformed)[0]

            # Basic recommendation logic
            if prediction == "High":
                recommendations = [
                    "Consult a healthcare provider immediately.",
                    "Maintain a healthy diet.",
                    "Exercise regularly.",
                    "Monitor your symptoms daily."
                ]
            elif prediction == "Medium":
                recommendations = [
                    "Get regular health checkups.",
                    "Maintain a balanced lifestyle.",
                    "Avoid smoking and alcohol."
                ]
            else:
                recommendations = [
                    "Keep up your good habits!",
                    "Continue regular physical activity.",
                    "Stay mindful of stress levels."
                ]

        except Exception as e:
            print(f"Error during prediction: {e}")
            prediction = "Error"
            recommendations = ["There was a problem processing your request. Please try again."]

    return render_template("index.html", features=feature_names, prediction=prediction, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
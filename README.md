<h1>Personalized Healthcare Risk Assessment and Recommendations</h1>

<p>
This project uses machine learning to assess personal health risk levels and provide tailored lifestyle recommendations. By analyzing clinical and lifestyle features, it identifies potential health issues early and supports preventive interventions.
</p>

<h2>📌 Objectives</h2>
<ul>
  <li>Predict individual health risk based on clinical and lifestyle attributes.</li>
  <li>Offer personalized health improvement suggestions based on input features.</li>
  <li>Build an interpretable machine learning model to assess health risks.</li>
  <li>Develop an interactive web interface for user input and results display.</li>
  <li>Deploy the solution on Render for public access.</li>
</ul>

<h2>🧰 Technologies Used</h2>
<ul>
  <li>Python, Pandas, NumPy, Scikit-learn</li>
  <li>Random Forest, XGBoost, Gradient Boosting, Extra Trees</li>
  <li>Flask for web app</li>
  <li>Plotly and Matplotlib for visualizations</li>
</ul>

<h2>📂 Dataset</h2>
<ul>
  <li>Synthetic dataset created to simulate real-world patient attributes.</li>
  <li>Features include: Age, Gender, BMI, Blood Pressure, Cholesterol, Physical Activity, etc.</li>
  <li>Target: Health Risk Level (Low, Medium, High)</li>
</ul>

<h2>📊 Analysis Highlights</h2>
<ul>
  <li>Data preprocessing, feature encoding, and scaling applied.</li>
  <li>Ensemble models trained with hyperparameter tuning.</li>
  <li>Performance evaluated using R² and RMSE scores.</li>
  <li>Feature importance analysis performed to drive personalized advice.</li>
</ul>

<h2>💡 Key Insights and Conclusions</h2>
<ul>
  <li>Models achieved strong predictive performance, with Extra Trees and XGBoost outperforming others.</li>
  <li>Top risk predictors: BMI, BP, Smoking, Cholesterol, Exercise, Sleep Quality.</li>
  <li>Web app allows real-time risk assessment with feedback.</li>
</ul>

<h2>📁 Repository Structure</h2>
<pre>
personalised_healthcare_recommendation/
│
├── static/
│   └── background.jpg             # Optional background image
│
├── templates/
│   └── predict.html               # Frontend form template
│
├── models/
│   ├── personalised_health_model.pkl     # Trained model
│   ├── preprocessor.pkl                  # Preprocessing pipeline
│   └── feature_names.pkl                 # Input feature names
│
├── personalised_healthcare_recommendation.ipynb  # Notebook with analysis and modeling
├── app.py                              # Flask application file
├── requirements.txt                    # Dependencies list
├── README.md                           # Project documentation
</pre>

<h2>🙏 Acknowledgements</h2>
<ul>
  <li>Synthetic data generation based on WHO/CDC real-world trends.</li>
  <li>Open-source tools from Scikit-learn, Flask, and Python community.</li>
</ul>

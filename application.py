from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

# ----------------------------------------
# Load data for populating form dropdowns
# ----------------------------------------
car = pd.read_csv('cleaned_car_data.csv')

# Adjust column names based on your CSV file
# If the car model is stored under 'model' instead of 'name', use 'model'
companies = sorted(car['company'].unique())
car_models = sorted(car['model'].unique())  # Changed from 'name' to 'model'
years = sorted(car['year'].unique(), reverse=True)
fuel_types = sorted(car['fuel_type'].unique())

# --------------------
# Initialize Flask app
# --------------------
app = Flask(__name__)

# --------------------------------------------
# Load the trained machine learning model
# --------------------------------------------
model = joblib.load('car_price_predictor.pkl')

# --------------------------------------------
# Load the columns used during model training
# --------------------------------------------
model_columns = joblib.load('model_columns.pkl')


# --------------------
# Home Route
# --------------------
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None  # Placeholder for predicted price

    if request.method == "POST":
        # Get form data
        company = request.form['company']
        car_model = request.form['car_model']
        fuel = request.form['fuel']
        year = int(request.form['year'])
        kms_driven = int(request.form['kms_driven'])

        # --------------------------
        # Prepare input for the model
        # --------------------------
        input_df = pd.DataFrame([[car_model, company, year, kms_driven, fuel]],
                                columns=['model', 'company', 'year', 'kms_driven', 'fuel_type'])

        # One-hot encode input and align with training columns
        input_encoded = pd.get_dummies(input_df)
        input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

        # --------------------------
        # Predict price using model
        # --------------------------
        pred = model.predict(input_encoded)[0]
        prediction = f"{pred:,.2f}"  # Format to 2 decimal places with comma separator

    # ------------------------
    # Render the form template
    # ------------------------
    return render_template("index.html",
                           companies=companies,
                           car_models=car_models,
                           years=years,
                           fuel_types=fuel_types,
                           prediction=prediction)


# --------------------------
# Run the Flask app locally
# --------------------------
if __name__ == "__main__":
    app.run(debug=True)

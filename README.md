# 🚗 Car Price Prediction Web App using Machine Learning

This project was completed as part of my **AI/ML Internship** at **InternPe**. The task involved building and deploying a machine learning model that predicts the selling price of a used car based on features like brand, model, year, fuel type, and kilometers driven.

---

## 📌 Task Objective

Develop and deploy a regression-based ML model to predict used car prices using historical data. The final solution includes a **Flask-powered web application** with real-time prediction functionality.

---

## 🛠️ Technologies Used

- Python  
- Flask  
- HTML/CSS (Jinja templating)  
- Jupyter Notebook  
- NumPy  
- Pandas  
- scikit-learn  
  - Random Forest Regressor  
  - Train-Test Split  
  - Evaluation Metrics  
- joblib (for saving/loading models)

---

## 📁 Project Structure

```

car-price-predictor/
│
├── app.py                      # Flask application script
├── cleaned\_car\_data.csv        # Dataset used to train the model
├── car\_price\_predictor.pkl     # Trained ML model
├── model\_columns.pkl           # Feature columns used in training
├── templates/
│   └── index.html              # HTML template for the web interface
├── static/
│   └── style.css               # Optional styling file
├── README.md                   # Project documentation

```

---

## 🚘 Dataset Description

The dataset contains various attributes of used cars:

- **Company** – Brand (e.g., Maruti, Hyundai, etc.)  
- **Model** – Car model name  
- **Year** – Year of purchase  
- **Fuel Type** – Petrol, Diesel, LPG.  
- **KMs Driven** – Distance the car has traveled  
- **Selling Price** – Actual price (target variable)

---

## 🔄 ML Workflow

1. **Data Cleaning** – Removing outliers, missing values  
2. **Feature Selection** – Categorical & numerical separation  
3. **Model Training** – `RandomForestRegressor` from scikit-learn  
4. **Model Serialization** – Saved model using `joblib`  
5. **Web Interface** – Developed using Flask to accept inputs  
6. **Real-time Prediction** – Displayed via dynamic HTML template

---

## 🖥️ Web App Features

- User selects car details from dropdowns  
- Submits kilometers driven and other inputs  
- Receives **instant price prediction**  
- Simple and intuitive UI built with Jinja2 templating  

---

## 🔧 Future Scope

- Improve UI with better styling (Bootstrap/Materialize)  
- Add model comparison (XGBoost, Linear Regression, etc.)  
- Deploy on a cloud platform (Render, Heroku, Vercel)  
- Enable logging and exception handling for production  

---

## 🎓 Internship & Task Details

- **Internship Track**: Artificial Intelligence & Machine Learning  
- **Internship Provider**: InternPe  
- **Task Name**: Task 02 – Car Price Prediction & Deployment  
- **Environment**: Jupyter Notebook + Flask App (Local)

---

## 📬 Contact

**Difina George**  
📧 difina.georgecs@gmail.com  
📍 Kerala, India

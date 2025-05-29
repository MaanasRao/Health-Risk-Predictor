# Health Risk Predictor 🧠

A Flask web app that predicts the risk of Diabetes, Heart Disease, and Thyroid Disorders using trained machine learning models. Users input health data and receive predictions along with personalized health tips.

## 🚀 Features
- ✅ Disease-specific input forms
- 🧠 ML-based health risk predictions
- 💡 Personalized health tips
- 🌐 Flask-powered web interface

## 📁 Project Structure
```
Health Predictor/
├── app.py
├── model_diabetes.pkl
├── model_heart.pkl
├── model_thyroid.pkl
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── diabetes_form.html
│   ├── heart_form.html
│   ├── disease_selection.html
│   └── result.html
├── model_training/
│   ├── diabetes/
│   ├── heart/
│   └── thyroid/
├── README.md

```

## ⚙️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/health-risk-predictor.git
   cd health-risk-predictor
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask numpy
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Visit in browser**
   ```
   http://127.0.0.1:5000/
   ```

## 📌 Note
This project uses pre-trained `.pkl` models. Make sure they are in the same directory as `app.py`.

## 📜 License
This project is for educational/demo purposes. Feel free to use and modify it.

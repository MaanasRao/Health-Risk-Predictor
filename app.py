from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# # If it is giving an error then load the models by givng the absolute path
models = {}

try:
    models["diabetes"] = pickle.load(open("model_diabetes.pkl", "rb"))
except Exception as e:
    print("[ERROR] Could not load model_diabetes.pkl:", e)

try:
    models["heart"] = pickle.load(open("model_heart.pkl", "rb"))
except Exception as e:
    print("[ERROR] Could not load model_heart.pkl:", e)

try:
    models["thyroid"] = pickle.load(open("model_thyroid.pkl", "rb"))
except Exception as e:
    print("[ERROR] Could not load model_thyroid.pkl:", e)

# Health tips based on threshold values
TIPS = {
    "glucose": ("High glucose level detected. Reduce sugar intake, exercise regularly, and eat more fiber.", 140),
    "bloodpressure": ("Elevated blood pressure. Reduce salt intake and manage stress.", 90),
    "skinthickness": ("High skin thickness might indicate fat distribution issues. Monitor your BMI.", 40),
    "insulin": ("Elevated insulin levels. Consider low-carb diets and regular exercise.", 200),
    "bmi": ("High BMI. Adopt a balanced diet and stay physically active.", 30),
    "diabetespedigreefunction": ("High genetic risk. Regular checkups are recommended.", 0.7),
    "age": ("Older age increases risk. Prioritize regular screenings and a healthy lifestyle.", 50),
    "cp": ("Certain chest pain types increase risk. Consult a cardiologist.", 1),
    "chol": ("High cholesterol. Avoid fried foods and eat more fiber.", 200),
    "slope": ("Unusual slope pattern in ECG. Follow up with heart diagnostics.", 1),
    "on_thyroxine": ("You're on thyroxine, which may affect thyroid levels. Monitor dosage regularly.", 1),
    "TSH": ("High TSH may indicate hypothyroidism. Follow up with endocrinologist.", 4.0),
    "T3": ("Abnormal T3 levels can suggest thyroid dysfunction. Maintain regular testing.", 2.0),
    "TT4": ("Elevated TT4 may suggest hyperthyroidism. Discuss results with your doctor.", 150),
    "T4U": ("Unusual T4U level could indicate binding issues. Consult your doctor.", 1.5),
    "FTI": ("High FTI may point to hyperthyroid activity. Seek medical advice.", 120),
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/select_disease', methods=['POST'])
def select_disease():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    return render_template("disease_selection.html", name=name, age=age, gender=gender)

@app.route('/form', methods=['POST'])
def handle_form():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    disease = request.form['disease'].lower()

    if disease == 'diabetes':
        return render_template("diabetes_form.html", name=name, age=age, gender=gender)
    elif disease == 'heart':
        return render_template("heart_form.html", name=name, age=age, gender=gender)
    elif disease == 'thyroid':
        return render_template("thyroid_form.html", name=name, age=age, gender=gender)
    else:
        return "Invalid disease selected."

@app.route('/predict/<disease>', methods=['POST'])
def predict(disease):
    try:
        if disease == "diabetes":
            features = ['pregnancies', 'glucose', 'bloodpressure', 'skinthickness', 'insulin', 'bmi', 'diabetespedigreefunction', 'age']
            inputs = [float(request.form[f]) for f in features]
            model = models["diabetes"]
            prediction = model.predict([inputs])[0]

        elif disease == "heart":
            gender = request.form.get('gender')
            sex = 1 if gender.lower() == 'male' else 0
            age = float(request.form['age'])
            cp = float(request.form['cp'])
            chol = float(request.form['chol'])
            slope = float(request.form['slope'])

            inputs = [sex, age, cp, chol, slope]
            model = models["heart"]
            prediction = model.predict([inputs])[0]

        elif disease == "thyroid":
            gender = request.form.get('gender')
            sex = 1 if gender.lower() == 'male' else 0
            features = ['sex', 'age', 'on_thyroxine', 'TSH', 'T3', 'TT4', 'T4U', 'FTI']
            inputs = [sex]
            inputs.append(float(request.form['age']))
            inputs.append(float(request.form['on_thyroxine']))
            inputs += [float(request.form[f]) for f in features[3:]]
            model = models["thyroid"]
            prediction = model.predict([inputs])[0]

        else:
            return "Invalid disease"

        result = "High Risk" if prediction == 1 else "Low Risk"

        high_risk_tips = []
        for key, (tip, threshold) in TIPS.items():
            if key in request.form:
                try:
                    val = float(request.form[key])
                    if val > threshold:
                        high_risk_tips.append(f"{key.capitalize()}: {tip}")
                except ValueError:
                    continue

        disclaimer = "Note: This prediction may not be 100% accurate. Please consult a certified doctor for medical diagnosis and treatment."

    except Exception as e:
        result = f"(Prediction not available: {e})"
        high_risk_tips = []
        disclaimer = "Model execution error."

    return render_template("result.html",
                           prediction=result,
                           name=request.form.get('name', 'User'),
                           age=request.form.get('age'),
                           gender=request.form.get('gender', 'N/A'),
                           disease=disease.capitalize(),
                           tips=high_risk_tips,
                           disclaimer=disclaimer
                           )

if __name__ == '__main__':
    app.run(debug=True)
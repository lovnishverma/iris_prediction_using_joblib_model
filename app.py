from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("iris_model.joblib")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        swidth = float(request.form.get("swidth"))
        sheight = float(request.form.get("sheight"))
        pwidth = float(request.form.get("pwidth"))
        pheight = float(request.form.get("pheight"))
        prediction = model.predict([[swidth, sheight, pwidth, pheight]])
        return render_template("index.html", data=prediction[0])
    except Exception as e:
        return render_template("index.html", data=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run()
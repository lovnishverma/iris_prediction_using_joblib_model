from flask import Flask, render_template, request
from sklearn.linear_model import LogisticRegression
import joblib

app = Flask(__name__)

# Load the saved model
model = joblib.load("model.joblib")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        # It's safer to use float() instead of eval() for security reasons
        swidth = float(request.form.get("swidth"))
        sheight = float(request.form.get("sheight"))
        pwidth = float(request.form.get("pwidth"))
        pheight = float(request.form.get("pheight"))

        # Make prediction
        prediction = model.predict([[swidth, sheight, pwidth, pheight]])

        return render_template("index.html", data=prediction[0])

    except Exception as e:
        return render_template("index.html", data=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

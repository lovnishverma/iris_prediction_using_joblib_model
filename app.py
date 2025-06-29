from flask import Flask, render_template, request
from sklearn.linear_model import LogisticRegression
import joblib

app=Flask(__name__)


#predicting using saved model
model = joblib.load("iris_model.joblib")

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
  swidth=eval(request.form.get("swidth"))
  sheight=eval(request.form.get("sheight"))
  pwidth=eval(request.form.get("pwidth"))
  pheight=eval(request.form.get("pheight"))
  
  prediction = model.predict([[swidth,sheight,pwidth,pheight]])

  return render_template("index.html", data=prediction[0]))


if __name__ == '__main__':
  app.run()
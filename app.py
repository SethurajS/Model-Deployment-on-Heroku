from flask import Flask, render_template, request, url_for
import numpy as np
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=["POST", "GET"])
def predict():

    features = [int(feature) for feature in request.form.values()]
    feature_array = [np.array(features)]
    prediction = model.predict(feature_array)

    prediction = np.round(prediction[0], 2)

    return render_template('index.html', prediction='Your Salary will be around : ${}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
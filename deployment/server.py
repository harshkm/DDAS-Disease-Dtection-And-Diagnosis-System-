from flask import Flask, render_template, request,jsonify
import os
import random
# Keras
from keras.models import load_model

MODEL_PATH='C:/Users/kumar/OneDrive/Desktop/bhagwan malik h/final_minor_cov19/covid_model/new_covid_model_15.h5'


app=Flask(__name__)


@app.route('/',methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():

	audiofile=request.files['audiofile']
	#audio_path="./audio/" + audiofile.filename
	file_name= str(random.randint(0,100000))
	audiofile.save(file_name)

	model = load_model(MODEL_PATH)
	prediction=model.predict(file_name)

	os.remove(file_name)

	data=("prediction : ",prediction)

	return jsonify(data)

if __name__== '__main__':
	app.run(port=6969,debug=True)
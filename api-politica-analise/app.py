from flask import Flask, request,jsonify
import pickle
import joblib
import numpy as np
import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))     # set file directory path



#model = pickle.load(open(MODEL_PATH, 'rb')) # load the pickled model
model = joblib.load("models/politica.pkl")

dataset = pd.read_csv('./dataset/Tweets_Mg.csv',encoding='utf-8')

tweets = dataset["Text"].values
tweets

classes = dataset["Classificacao"].values
classes

# routes
@app.route('/prediction', methods=['GET'])  # submit the form
def make_prediction():
    vectorizer = CountVectorizer(analyzer = "word")
    freq_tweets = vectorizer.fit_transform(tweets)

    model = MultinomialNB()
    model.fit(freq_tweets, classes)
    mensagem = request.args['mensagem']
    testes = [mensagem]
    freq_testes = vectorizer.transform(testes)
    resultado = str(model.predict(freq_testes))
    return jsonify({"sentimento-da-mensagem":resultado})  # render the prediction page


if __name__ == '__main__':
    app.run(debug=True)

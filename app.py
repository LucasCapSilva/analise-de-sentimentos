from flask import Flask, request,jsonify

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

from googletrans import Translator
translator = Translator() # objeto tradutor
mensagemSentimento = ""

app = Flask(__name__)

@app.route('/prediction', methods=['POST'])  # rota via post passando pela body
def make_prediction_body():
    mensagem = request.json['mensagem'] # mensagem recebida atraves de parametro via get
    translations  = translator.translate(mensagem, dest='en') # método de traduçao da mensagem para ingles
    textTranslator = translations.text # capitura do texto traduzido
    score = analyser.polarity_scores(textTranslator) # avaliação de polaridade de sentimento da mensagem
    compound = (analyser.polarity_scores(textTranslator)['compound'])  # capitura da média do sentimento da mensagem
    if compound > 0:
      mensagemSentimento = "mensagem positiva"
    else:
      mensagemSentimento = "mensagem negativa"


    return jsonify({"mensagem":mensagem , "sentimento-da-mensagem": mensagemSentimento})  # retorno da mensagem

@app.route('/predictionParamter', methods=['GET'])  # rota via get passando parametro
def make_prediction():
    mensagem = request.args['mensagem'] # mensagem recebida atraves de parametro via get
    translations  = translator.translate(mensagem, dest='en') # método de traduçao da mensagem para ingles
    textTranslator = translations.text # capitura do texto traduzido
    score = analyser.polarity_scores(textTranslator) # avaliação de polaridade de sentimento da mensagem
    compound = (analyser.polarity_scores(textTranslator)['compound'])  # capitura da média do sentimento da mensagem
    if compound > 0:
      mensagemSentimento = "mensagem positiva"
    else:
      mensagemSentimento = "mensagem negativa"


    return jsonify({"mensagem":mensagem , "sentimento-da-mensagem": mensagemSentimento})  # retorno da mensagem

if __name__ == '__main__':
    app.run(debug=True)
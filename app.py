import requests
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods =["POST"])
def main():
    data = request.get_json(silent=True)

    intentName = data["queryResult"]["intent"]["displayName"]
    nome = data["queryResult"]["parameters"]["nome"]
    pedido = data["queryResult"]["parameters"]["pedido"]
    
#intent name Informações sobre sua encomenda

    if intentName =="Informações sobre sua encomenda":

        data["fulfillmentText"] = f"Sr {nome}, Aguarde um momento\
            Estaremos te passando informações do seu pedido {pedido} em breve!"
        
    elif intentName == "Cardapio":
        data["fulfillmentText"] = f"Sr {nome} aqui está nossas opções de cardápio"
    return jsonify(data)

if __name__ =="__main__":
    app.run(debug=False)

from flask import Flask, make_response, jsonify, request
from bd import Carros 

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros',methods = ['GET']) # ROTA DA API, GET Lista os carros
def get_carros():
    return make_response( 
        jsonify(
            message= 'Lista de carros.', 
            data= Carros
        )
    )

@app.route('/carros', methods = ['POST']) # POST Cadastra os carros
def create_carro(): 
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            message = 'Carro cadastrado com sucesso',
            carro = carro
        )
    )
app.run() 
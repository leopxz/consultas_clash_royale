from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Conexão com o MongoDB
client = MongoClient('mongodb+srv://pxleonarddo:Minhasenha3@royall.6xl73.mongodb.net/')
db = client['royall']

from datetime import datetime

def converter_data_para_string(data_str):
    data = datetime.strptime(data_str, '%Y-%m-%d')
    return data.strftime('%Y-%m-%d %H:%M:%S+00:00')

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/porcentagem_vitorias_derrotas', methods=['GET'])
def porcentagem_vitorias_derrotas():
    carta = int(request.args.get('carta'))
    inicio = request.args.get('inicio')  # Captura a string diretamente
    fim = request.args.get('fim')  # Captura a string diretamente

    # Converter as datas para string
    inicio_str = converter_data_para_string(inicio)
    fim_str = converter_data_para_string(fim)

    result = db.battles.aggregate([
        {
            '$match': {
                'battleTime': {'$gte': inicio_str, '$lte': fim_str},
                '$or': [
                    {'winner.cards.list': carta},
                    {'loser.cards.list': carta}
                ]
            }
        },
        {
            '$group': {
                '_id': None,
                'totalBattles': {'$sum': 1},
                'victories': {
                    '$sum': {'$cond': [{'$in': [carta, '$winner.cards.list']}, 1, 0]}
                },
                'defeats': {
                    '$sum': {'$cond': [{'$in': [carta, '$loser.cards.list']}, 1, 0]}
                }
            }
        },
        {
            '$project': {
                'percentage_victories': {'$multiply': [{'$divide': ['$victories', '$totalBattles']}, 100]},
                'percentage_defeats': {'$multiply': [{'$divide': ['$defeats', '$totalBattles']}, 100]}
            }
        }
    ])
    
    return jsonify(list(result))

# 2. Liste os decks completos que produziram mais de X% de vitórias
@app.route('/decks_vitoriosos', methods=['GET'])
def decks_vitoriosos():
    porcentagem = float(request.args.get('porcentagem'))
    inicio = request.args.get('inicio')
    fim = request.args.get('fim')

    inicio_str = converter_data_para_string(inicio)
    fim_str = converter_data_para_string(fim)

    result = db.battles.aggregate([
        {
            '$match': {
                'battleTime': {'$gte': inicio_str, '$lte': fim_str}
            }
        },
        {
            '$group': {
                '_id': '$winner.cards.list',
                'totalBattles': {'$sum': 1},
                'victories': {
                    '$sum': {'$cond': [{'$eq': ['$winner.cards.list', '$_id']}, 1, 0]}
                }
            }
        },
        {
            '$match': {
                '$expr': {
                    '$gt': [{'$multiply': [{'$divide': ['$victories', '$totalBattles']}, 100]}, porcentagem]
                }
            }
        },
        {
            '$project': {
                'deck': '$_id',
                'win_rate': {'$multiply': [{'$divide': ['$victories', '$totalBattles']}, 100]}
            }
        }
    ])
    
    return jsonify(list(result))

# Outros métodos podem ser ajustados da mesma forma para manter a consistência


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {'id':0,
    'nome':'Gabriel',
     'habilidade':['Python','Django']
     },
    {'id':1,
        'nome':'taltal',
     'habilidade':['Python','Flask']
     }
]

#devolve um desenvolvedor pelo ID, tambem deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não exixte'.format(id)
            response = {'status': 'ERROR','mensagem': mensagem}
        except Exception:
            mensagem = "Erro desconhecido, Procure o ADM da API"
            response = {'status':'erro','mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'registro excluido'})


#Lista todos os desenvolvedores e permite registrar novos desevolvedores
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)

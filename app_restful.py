from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades
app = Flask(__name__)
api = Api(app)


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


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não exixte'.format(id)
            response = {'status': 'ERROR', 'mensagem': mensagem}
        except Exception:
            mensagem = "Erro desconhecido, Procure o ADM da API"
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluido'}


class Lista_Desenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

    def get(self):
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_Desenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)

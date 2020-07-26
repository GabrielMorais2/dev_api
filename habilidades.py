from flask_restful import Resource, request
import json

lista_habilidades = ['python', 'java', 'php', 'REST']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

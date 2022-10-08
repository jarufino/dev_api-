from flask import Flask
from flask_restful import Resource, Api

from requests import request

from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Julio',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Patricia',
        'habilidades': ['Java', 'JavaScript']
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, fale com o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = request.data
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro Excluído'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = request.data
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])


# api.add_resource(Desenvolvedor, '/dev/<int:id>/')
# api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades,'/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)

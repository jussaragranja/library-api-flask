from flask_restplus import fields
from src.server.instance import server


book = server.api.model('Book', {
    'id': fields.Integer(required=True, description='Id do registro.'),
    'title': fields.String(required=True, min_Length=1, max_Length=200, description='Titulo do Livro')
})

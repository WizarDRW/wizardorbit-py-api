from flask_restplus import Namespace, fields
from sqlalchemy.ext.declarative import api


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class GlobalWarningDto:
    api = Namespace('global-warning', description='')
    globalwarning = api.model('global', {})


class ChapterDto:
    api = Namespace('chapter', description='')
    chapter = api.model('chapter', {
        '_id': fields.String(required=True, description=''),
        'impressions': fields.Nested(fields.String, description='', required=True)
    })

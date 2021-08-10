from flask.globals import request
from flask_restplus import Namespace, fields


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


class InfoContentDto:
    api = Namespace('infocontent', description='')
    info_content = api.model('infocontents', {
        'contents': fields.List(fields.Nested(api.model('content', {
            '_id': fields.String(required=True, description=''),
            'impressions': fields.List(fields.Nested(api.model('impression', {
                "ip": fields.String(required=True),
                "count": fields.Integer(required=True)
            })))
        }))),
        'limit': fields.Integer(required=True)
    })

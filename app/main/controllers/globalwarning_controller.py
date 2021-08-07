from flask.json import jsonify
from flask import request
from flask_restplus import Resource

from ..utils.dto import GlobalWarningDto

api = GlobalWarningDto.api
_global = GlobalWarningDto.globalwarning

@api.route('/')
class GlobalWarning(Resource):
    @api.doc('list_of_global_warnings')
    @api.marshal_list_with(_global, envelope='data')
    def get(self, params=""):
        """List all registered users"""
        return jsonify(request.get(url=self.baseUrl, params=params).json())
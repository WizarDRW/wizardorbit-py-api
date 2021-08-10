from flask.globals import request
from flask.json import jsonify
from flask import request as rq
from flask_restplus import Resource
import requests as reqs

from ..utils.dto import GlobalWarningDto

api = GlobalWarningDto.api

@api.route('/<warn>')
@api.param('warn', 'grobal warning')
class GlobalWarning(Resource):
    @api.doc('list_of_global_warnings')
    def get(self, warn="co2"):
        """List all registered users"""
        if warn == 'co2':
            return jsonify(reqs.get(url='https://global-warming.org/api/co2-api').json()['co2'])
        elif warn == 'mt':
            return jsonify(reqs.get(url='https://global-warming.org/api/methane-api').json()['methane'])
        elif warn == 'tm':
            return jsonify(reqs.get(url='https://global-warming.org/api/temperature-api').json()['temperature'])
        elif warn == 'no':
            return jsonify(reqs.get(url='https://global-warming.org/api/nitrous-oxide-api').json()['nitrous'])
        elif warn == 'ar':
            return jsonify(reqs.get(url='https://global-warming.org/api/arctic-api').json()['arctic'])
        return False
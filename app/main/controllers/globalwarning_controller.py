from flask.json import jsonify
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
            return self.co2()
        elif warn == 'mt':
            return self.methane()
        elif warn == 'tm':
            return self.temperature()
        elif warn == 'no':
            return self.nitrous()
        elif warn == 'ar':
            return self.arctic()
        return False

    @staticmethod
    def co2():
        return jsonify(reqs.get(url='https://global-warming.org/api/co2-api').json()['co2'])
    @staticmethod
    def methane():
        return jsonify(reqs.get(url='https://global-warming.org/api/methane-api').json()['methane'])
    @staticmethod
    def temperature():
        return jsonify(reqs.get(url='https://global-warming.org/api/temperature-api').json()['temperature'])
    @staticmethod
    def nitrous():
        return jsonify(reqs.get(url='https://global-warming.org/api/nitrous-oxide-api').json()['nitrous'])
    @staticmethod
    def arctic():
        return jsonify(reqs.get(url='https://global-warming.org/api/arctic-api').json()['arctic'])
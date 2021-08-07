from flask.json import jsonify
from flask import request
from flask_restplus import Resource

from ..utils.dto import ChapterDto

api = ChapterDto.api

@api.route('/global-warning')
class ChapterController(Resource):
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def createdb(self):
        pass

    def connection(self):
        pass

    def getAll(self, params=""):
        return jsonify(reqs.get(url=self.baseUrl, params=params).json())
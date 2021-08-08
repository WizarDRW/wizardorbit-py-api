from flask.json import jsonify
from flask import request
from flask_restplus import Resource
import pandas as pd
import numpy as np

from ..utils.dto import ChapterDto

api = ChapterDto.api
_chapter = ChapterDto.chapter

@api.route('/', methods=['POST'])
class ChapterStatistics(Resource):
    @api.doc("chapter statistics")
    @api.expect(_chapter, validate=True)
    @api.response(200, '')
    def post(self, params=""):
        """Post and statistics"""
        data = request.json['chapters']
        dt = pd.Series(data)
        print(request)
        return dt.size
from logging import log
from flask.json import jsonify
from flask import request
from flask_restplus import Resource
import pandas as pd
import numpy as np

from ..utils.dto import ChapterDto

api = ChapterDto.api
_chapter = ChapterDto.chapter


@api.route('/')
class ChapterStatistics(Resource):
    @api.doc("chapter statistics")
    @api.expect(_chapter, validate=True)
    @api.response(200, '')
    def post(self, params=""):
        """Post and statistics"""
        data = request.json['chapters']
        for item in data:
            series = pd.Series(item['impressions'])
            item['imp_len'] = self.content_len(series)
            item['imp_std'] = np.std([s['count'] for s in series])
        result = sorted(data,key=lambda x: x['imp_std'])[:request.json['limit']]
        return jsonify(result)

    def content_len(self, content):
        return pd.Series(content).size

    def content_std(self, series):
        pass 

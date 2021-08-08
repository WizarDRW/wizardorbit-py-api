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
            result = self.content_len(series)
            item['imp_len'] = result
            res_std = np.std([s['count'] for s in series])
            item['imp_std'] = res_std
        return data

    def content_len(self, content):
        return pd.Series(content).size

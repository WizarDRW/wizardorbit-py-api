from logging import log
from flask.json import jsonify
from flask import request
from flask_restplus import Resource
import pandas as pd
import numpy as np

from ..utils.dto import InfoContentDto

api = InfoContentDto.api
_chapter = InfoContentDto.info_content


@api.route('/')
class InfoContentStatistics(Resource):
    @api.doc("chapter statistics")
    @api.expect(_chapter, validate=True)
    @api.response(200, '')
    def post(self, params=""):
        """Post and statistics"""
        data = request.json['contents']
        for item in data:
            series = pd.Series(item['impressions'])
            item['imp_len'] = self.content_len(series)
            item['imp_mean'] = np.mean([s['count'] for s in series])
            item['imp_std'] = self.content_std(series)
            item['point'] = item['imp_len'] - item['imp_std'] + item['imp_mean']
        result = sorted(data,key=lambda x: x['point'], reverse=True)[:request.json['limit']]
        return jsonify(result)

    def content_len(self, content):
        return pd.Series(content).size

    def content_std(self, series):
        return np.std([s['count'] for s in series]) 

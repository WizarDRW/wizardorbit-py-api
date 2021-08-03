from flask.json import jsonify
import requests as reqs

class GlobalWarning(object):
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def getAll(self, params=""):
        return jsonify(reqs.get(url=self.baseUrl, params=params).json())
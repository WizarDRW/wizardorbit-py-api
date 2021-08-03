from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import routers.globalwarning as globalWarning
# from controllers.note import *

app = Flask(__name__)
api = Api(app)

# Setup the Api resource routing

api.add_resource(globalWarning.nitrousOxide())

# api.add_resource(NoteResource, '/notes/', endpoint='notes')

if __name__ == '__main__':
    app.run(debug=True)

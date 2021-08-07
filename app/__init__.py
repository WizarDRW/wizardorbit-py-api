from flask_restplus import Api
from flask import Blueprint

from .main.controllers.user_controller import api as user_ns
from .main.controllers.globalwarning_controller import api as global_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(global_ns, path='/global')
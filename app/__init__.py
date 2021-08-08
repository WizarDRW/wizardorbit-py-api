from flask_restplus import Api
from flask import Blueprint

from .main.controllers.user_controller import api as user_ns
from .main.controllers.globalwarning_controller import api as global_ns
from .main.controllers.chapter_controller import api as chapter_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title="Wizard's Orbit",
          version='1.0',
          description=''
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(global_ns, path='/global')
api.add_namespace(chapter_ns, path='/chapter')
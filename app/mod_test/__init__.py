from flask import Blueprint

mod_test = Blueprint('test', __name__, url_prefix='/test')

from . import  controller

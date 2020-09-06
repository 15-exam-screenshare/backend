from flask import Blueprint

mod_test = Blueprint('test', __name__)

from . import controller


from flask import Blueprint

system_bp = Blueprint("system", __name__)

from . import routes  # noqa

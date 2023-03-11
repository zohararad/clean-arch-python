from flask import Blueprint
from app.colormind_svc import ColorMindSvc
from adapters.colormind_repo import ColorMindRepo


repo = ColorMindRepo()
color_mind_svc = ColorMindSvc(repo)
blueprint = Blueprint('api', __name__)

from . import colormind_api

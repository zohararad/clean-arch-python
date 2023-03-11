from . import blueprint, color_mind_svc
from flask import request
import json


@blueprint.route("/api/v1/models", methods=['GET'])
def models():
    result = color_mind_svc.models()
    return result


@blueprint.route("/api/v1/random", methods=['GET'])
def random():
    model = request.args.get('model', 'default')
    result = color_mind_svc.random(model)
    return result


@blueprint.route("/api/v1/suggest", methods=['GET'])
def suggest():
    model = request.args.get('model', 'default')
    colors = request.args.get('colors', '["N","N","N","N","N"]')
    result = color_mind_svc.suggest(model, json.loads(colors))
    return result

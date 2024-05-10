import logging
import json

from src.recipe_controller import RecipeController
from ingredient_controller import IngredientController

from flask import Flask, jsonify, request, abort, Response
from flask_cors import CORS, cross_origin

flask_api = Flask(__name__)
CORS(flask_api)


@flask_api.route('/api/sayhello', methods=['GET'])
def get_sayhello():	
    controller = RecipeController()

    res = controller.fetch_recipes()

    return Response(json.dumps(res, default=lambda x: x.__dict__), status=200, mimetype="application/json")


@flask_api.route('/api/recipe', methods=['GET'])
def get_recipe():
    try:
        controller = RecipeController()

        res = { 'recipes:': controller.get_recipes() }

        return Response(json.dumps(res, default=lambda x: x.__dict__), status=200, mimetype="application/json")
    except Exception as e:
        abort(500, e)

@flask_api.route('/api/recipe', methods=['POST'])
def post_recipe():
    try:
        if not request.json:
            abort(400)

        controller = RecipeController()

        data = controller.post_recipe(request.json)

        return Response(json.dumps(data, default=lambda x: x.__dict__), status=200, mimetype="application/json")
    except Exception as e:
        abort(500, e)

@flask_api.route('/api/recipe/<id>', methods=['PUT'])
def put_recipe(id):
    try:
        if not request.json:
            abort(400)

        controller = RecipeController()

        data = controller.put_recipe(id,request.json)

        return Response(json.dumps(data, default=lambda x: x.__dict__), status=200, mimetype="application/json")
    except Exception as e:
        abort(500, e)

@flask_api.route('/api/recipe/<id>', methods=['DELETE'])
def delete_recipe(id):
    try:
        if not id:
            abort(400)

        controller = RecipeController()

        data = controller.delete_recipe(id)

        return Response(json.dumps(data, default=lambda x: x.__dict__), status=200, mimetype="application/json")
    except Exception as e:
        abort(500, e)

@flask_api.route('/ingredient', methods=['POST'])
def post_ingredient():
    """Add ingredient to Pantry"""
    try:
        if not request.json:
            abort(400)

        controller = IngredientController()

        data = controller.post_ingredient(request.json)

        return Response(json.dumps(data, default=lambda x: x.__dict__), status=200, mimetype="application/json")
    except Exception as e:
        abort(500, e)

@flask_api.errorhandler(500)
def server_error(e):
    logging.exception('error during request')
    return """
    Internal error occurred: <pre>{}</pre>
    See logs.
    """.format(e), 500

if __name__ == '__main__':
    flask_api.run(debug=True)

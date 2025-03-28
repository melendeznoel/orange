import json
import logging
from flask import Flask, request, abort, Response
from flask_cors import CORS

from .recipe_controller import RecipeController
from .ingredient_controller import IngredientController

flask_api = Flask(__name__)
CORS(flask_api)


@flask_api.route('/recipe', methods=['GET'])
def get_recipe():
    try:
        controller = RecipeController()

        res = { 'recipes:': controller.get_recipes() }

        recipes = json.dumps(res, default=lambda x: x.__dict__)

        return Response(recipes, status=200, mimetype="application/json")
    except Exception as e:
        abort(500, e)

@flask_api.route('/recipe', methods=['POST'])
def post_recipe():
    try:
        if not request.json:
            abort(400)

        controller = RecipeController()

        data = controller.post_recipe(request.json)

        recipe = json.dumps(data, default=lambda x: x.__dict__)

        return Response(recipe, status=200, mimetype="application/json")
    except Exception as e:
        abort(500, e)

@flask_api.route('/recipe/<id>', methods=['PUT'])
def put_recipe(id):
    try:
        if not request.json:
            abort(400)

        controller = RecipeController()

        data = controller.put_recipe(id,request.json)

        recipe = json.dumps(data, default=lambda x: x.__dict__)

        return Response(recipe, status=200, mimetype="application/json")
    except Exception as e:
        abort(500, e)

@flask_api.route('/recipe/<id>', methods=['DELETE'])
def delete_recipe(id):
    try:
        if not id:
            abort(400)

        controller = RecipeController()

        data = controller.delete_recipe(id)

        recipe = json.dumps(data, default=lambda x: x.__dict__)

        return Response(recipe, status=200, mimetype="application/json")
    except Exception as e:
        abort(500, e)

@flask_api.route('/ingredient', methods=['POST'])
def post_ingredient():
    """Add ingredient to Pantry"""
    try:
        if not request.json:
            abort(400)

        controller = IngredientController()

        data = controller.create_ingredient(request.json)

        ingredient = json.dumps(data, default=lambda x: x.__dict__)

        return Response(ingredient, status=200, mimetype="application/json")
    except Exception as e:
        abort(500, e)

@flask_api.route('/ingredient/_search', methods=['POST'])
def post_search_ingredient():
    """Search ingredient"""
    try:
        if not request.json:
            abort(400)

        controller = IngredientController()

        data = controller.search_ingredient(request.json)

        ingredient = json.dumps(data, default=lambda x: x.__dict__)

        return Response(ingredient, status=200, mimetype="application/json")
    except Exception as e:
        abort(500, e)

@flask_api.errorhandler(500)
def server_error(e):
    """Catch all api errors"""
    logging.exception('error during request')

    return f'Internal error occurred: <pre>{e}</pre>See logs.', 500

if __name__ == '__main__':
    flask_api.run(debug=True)

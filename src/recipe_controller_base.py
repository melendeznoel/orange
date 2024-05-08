from .recipe_service import RecipeService
from .recipe_provider import RecipeProvider

class RecipeControllerBase:
    def __init__(self):
        self.recipeService = RecipeService()
        self.recipeProvider = RecipeProvider()
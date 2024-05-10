"""Controller"""
import logging

class IngredientController:
    """Ingredient Controller"""
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def post_ingredient(self, ingredient):
        """New Ingredient"""
        pass

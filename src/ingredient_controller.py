"""Controller"""
import logging

from .fhir.fhir_nutrition_product_ingredient import FhirNutritionProductIngredient

class IngredientController:
    """Ingredient Controller"""
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def create_ingredient(self, ingredient):
        """New Ingredient"""
        return [FhirNutritionProductIngredient.from_dict(y) for y in ingredient.get("ingredient")]

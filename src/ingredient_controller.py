"""Controller"""
import logging

from .fhir.fhir_nutrition_product_ingredient import FhirNutritionProductIngredient
from .fhir_service import FhirService

class IngredientController:
    """Ingredient Controller"""
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def create_ingredient(self, ingredient):
        """New Ingredient"""
        fhir_service = FhirService()

        ing = FhirNutritionProductIngredient.from_dict(ingredient)

        fhir_resource = fhir_service.save_resource(ing)

        return fhir_resource

"""A food or supplement that is consumed by patients."""
from typing import List
from typing import Any
from dataclasses import dataclass
from fhir_nutrition_product_nutrient import FhirNutritionProductNutrient
from fhir_nutrition_product_instance import FhirNutritionProductInstance
from fhir_nutrition_product_ingredient import FhirNutritionProductIngredient
from fhir_nutrition_product_characteristic import FhirNutritionProductCharacteristic
from fhir_annotation import FhirAnnotation
import json

@dataclass
class FhirNutritionProduct:
    """A food or supplement"""
    resourceType: str
    code: str
    status: str
    category: str
    manufacturer: str
    nutrient: List[FhirNutritionProductNutrient]
    ingredient: List[FhirNutritionProductIngredient]
    knownAllergen: str
    characteristic: List[FhirNutritionProductCharacteristic]
    instance: List[FhirNutritionProductInstance]
    note: List[FhirAnnotation]

    @staticmethod
    def from_dict(obj: Any) -> 'FhirNutritionProduct':
        _resourceType = str(obj.get("resourceType"))
        _code = str(obj.get("code"))
        _status = str(obj.get("status"))
        _category = str(obj.get("category"))
        _manufacturer = str(obj.get("manufacturer"))
        _nutrient = [FhirNutritionProductNutrient.from_dict(y) for y in obj.get("nutrient")]
        _ingredient = [FhirNutritionProductIngredient.from_dict(y) for y in obj.get("ingredient")]
        _knownAllergen = str(obj.get("knownAllergen"))
        _characteristic = [FhirNutritionProductCharacteristic.from_dict(y) for y in obj.get("characteristic")]
        _instance = [FhirNutritionProductInstance.from_dict(y) for y in obj.get("instance")]
        _note = [FhirAnnotation.from_dict(y) for y in obj.get("note")]
        return FhirNutritionProduct(_resourceType, _code, _status, _category, _manufacturer, _nutrient, _ingredient, _knownAllergen, _characteristic, _instance, _note)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)

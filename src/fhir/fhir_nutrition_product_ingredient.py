"""Ingredient contained in this product"""
from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class FhirNutritionProductIngredient:
    """Ingredient of product"""
    item: str
    amount: str

    @staticmethod
    def from_dict(obj: Any) -> 'FhirNutritionProductIngredient':
        """Mapper"""
        _item = str(obj.get("item"))
        _amount = str(obj.get("amount"))

        return FhirNutritionProductIngredient(_item, _amount)

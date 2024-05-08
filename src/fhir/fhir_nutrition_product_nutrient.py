"""A product used for nutritional purposes (i.e. food or supplement)"""
from typing import Any
from dataclasses import dataclass

@dataclass
class FhirNutritionProductNutrient:
    """A food or supplement that is consumed by patients."""
    item: str
    amount: str

    @staticmethod
    def from_dict(obj: Any) -> 'FhirNutritionProductNutrient':
        """Mapper"""
        _item = str(obj.get("item"))
        _amount = str(obj.get("amount"))

        return FhirNutritionProductNutrient(_item, _amount)

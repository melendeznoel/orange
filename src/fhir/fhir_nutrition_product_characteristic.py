"""Specifies descriptive properties of the nutrition product"""
from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class FhirNutritionProductCharacteristic:
    """Descriptive properties of the nutrition product"""
    type: str
    valueCodeableConcept: str
    valueString: str
    valueQuantity: str
    valueBase64Binary: str
    valueAttachment: str
    valueBoolean: bool

    @staticmethod
    def from_dict(obj: Any) -> 'FhirNutritionProductCharacteristic':
        """Mapper"""
        _type = str(obj.get("type"))
        _valueCodeableConcept = str(obj.get("valueCodeableConcept"))
        _valueString = str(obj.get("valueString"))
        _valueQuantity = str(obj.get("valueQuantity"))
        _valueBase64Binary = str(obj.get("valueBase64Binary"))
        _valueAttachment = str(obj.get("valueAttachment"))
        _valueBoolean = bool(obj.get("valueBoolean"))

        return FhirNutritionProductCharacteristic(_type, _valueCodeableConcept, _valueString, _valueQuantity, _valueBase64Binary, _valueAttachment, _valueBoolean)

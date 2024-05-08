"""Specifies descriptive properties of the nutrition product"""
from typing import List, Any
from dataclasses import dataclass

@dataclass
class FhirNutritionProductCharacteristic:
    """Descriptive properties of the nutrition product"""
    type: str
    value_codeable_concept: str
    value_string: str
    value_quantity: str
    value_base64_binary: str
    value_attachment: str
    value_boolean: bool

    @staticmethod
    def from_dict(obj: Any) -> 'FhirNutritionProductCharacteristic':
        """Mapper"""
        _type = str(obj.get("type"))
        _value_codeable_concept = str(obj.get("valueCodeableConcept"))
        _value_string = str(obj.get("valueString"))
        _value_quantity = str(obj.get("valueQuantity"))
        _value_base64_binary = str(obj.get("valueBase64Binary"))
        _value_attachment = str(obj.get("valueAttachment"))
        _value_boolean = bool(obj.get("valueBoolean"))

        return FhirNutritionProductCharacteristic(_type, _value_codeable_concept, _value_string, _value_quantity, _value_base64_binary, _value_attachment, _value_boolean)

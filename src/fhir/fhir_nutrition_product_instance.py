"""One or several physical instances or occurrences of the nutrition product"""
from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class FhirNutritionProductInstance:
    """Physical instances or occurrences of the nutrition product"""
    quantity: str
    identifier: str
    name: str
    lotNumber: str
    expiry: str
    useBy: str
    biologicalSourceEvent: str

    @staticmethod
    def from_dict(obj: Any) -> 'FhirNutritionProductInstance':
        """Mapper"""
        _quantity = str(obj.get("quantity"))
        _identifier = str(obj.get("identifier"))
        _name = str(obj.get("name"))
        _lotNumber = str(obj.get("lotNumber"))
        _expiry = str(obj.get("expiry"))
        _useBy = str(obj.get("useBy"))
        _biologicalSourceEvent = str(obj.get("biologicalSourceEvent"))

        return FhirNutritionProductInstance(_quantity, _identifier, _name, _lotNumber, _expiry, _useBy, _biologicalSourceEvent)

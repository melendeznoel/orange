"""One or several physical instances or occurrences of the nutrition product"""
from typing import List, Any
from dataclasses import dataclass
from fhir_identifier import FhirIdentifier

@dataclass
class FhirNutritionProductInstance:
    """Physical instances or occurrences of the nutrition product"""
    quantity: str
    identifier: List[FhirIdentifier]
    name: str
    lot_number: str
    expiry: str
    use_by: str
    biological_source_event: str

    @staticmethod
    def from_dict(obj: Any) -> 'FhirNutritionProductInstance':
        """Mapper"""
        _quantity = str(obj.get("quantity"))
        _identifier = [FhirIdentifier.from_dict(y) for y in obj.get("FhirIdentifier")]
        _name = str(obj.get("name"))
        _lot_number = str(obj.get("lotNumber"))
        _expiry = str(obj.get("expiry"))
        _use_by = str(obj.get("useBy"))
        _biological_source_event = str(obj.get("biologicalSourceEvent"))

        return FhirNutritionProductInstance(_quantity, _identifier, _name, _lot_number, _expiry, _use_by, _biological_source_event)

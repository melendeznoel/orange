"""Concept - reference to a terminology or just text"""
class FhirCoding:
    """Code defined by a terminology system"""
    system: str
    code: str

    def __init__(self, system: str, code: str) -> None:
        self.system = system
        self.code = code

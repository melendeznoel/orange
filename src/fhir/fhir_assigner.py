"""Organization that issued id (may be just text)"""
class FhirAssigner:
    """Reference(Organization)"""
    display: str

    def __init__(self, display: str) -> None:
        self.display = display

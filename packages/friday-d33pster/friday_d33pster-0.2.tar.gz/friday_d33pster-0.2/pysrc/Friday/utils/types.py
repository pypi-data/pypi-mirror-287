from typing import Any

class OnlyTrue:
    """Only True class: `return type where the value is decided and only True`"""
    def __init__(self):
        """`Only True class: `return type where the value is decided and only True``"""
        self.value = True
    
    @property
    def get(self) -> Any:
        """`Always returns True`"""
        return self.value
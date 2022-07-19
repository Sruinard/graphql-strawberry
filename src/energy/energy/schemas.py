import strawberry as sb
from typing import List, Optional

@sb.type
class Country:
    name: str
    emission: float

@sb.type
class Industry:
    name: str
    emission: float
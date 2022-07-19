from dataclasses import dataclass


@dataclass
class Industry:
    name: str
    emission: float

@dataclass
class Country:
    name: str
    emission: float



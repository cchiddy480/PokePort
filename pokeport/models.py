from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class PokemonCard:
    id: Optional[int] = None
    name: str = ""
    set_name: str = ""
    rarity: str = ""
    purchase_price: float = 0.0
    market_value: float = 0.0
    grading_score: float = 0.0
    image_url: Optional[str] = None

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "PokemonCard":
        return PokemonCard(
            id=data.get("id"),
            name=data.get("name", ""),
            set_name=data.get("set_name", ""),
            rarity=data.get("rarity", ""),
            purchase_price=data.get("purchase_price", 0.0),
            market_value=data.get("market_value", 0.0),
            grading_score=data.get("grading_score", 0.0),
            image_url=data.get("image_url")
        )

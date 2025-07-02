# models.py
# This file defines the data model for a Pokemon card in the PokePort application.
# The model uses Python's dataclass to make it easy to store and manage card data.

from dataclasses import dataclass, asdict
from typing import Optional

# The PokemonCard class represents a single Pokemon card in the collection.
# It stores all the important information about the card.
@dataclass
class PokemonCard:
    id: Optional[int] = None  # The unique ID for the card (set by the database)
    name: str = ""            # The name of the Pokemon (e.g., "Pikachu")
    set_name: str = ""        # The set the card belongs to (e.g., "Base Set")
    rarity: str = ""          # The rarity of the card (e.g., "Common", "Rare")
    purchase_price: float = 0.0  # The price you paid for the card
    market_value: float = 0.0    # The current market value of the card
    grading_score: float = 0.0   # The grading score (e.g., 8.5 out of 10)
    image_url: Optional[str] = None  # Optional: a link to an image of the card

    def to_dict(self):
        """
        Convert the PokemonCard object to a dictionary.
        This is useful for saving the card data or sending it to other parts of the program.
        """
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "PokemonCard":
        """
        Create a PokemonCard object from a dictionary.
        This is useful when loading card data from a file or database.
        """
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

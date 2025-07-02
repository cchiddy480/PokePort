"""
roi.py - Handles ROI (Return on Investment) calculations for Pokémon cards.

Why this file exists:
> Tracking ROI is important for collectors who care about the value of their collection. This module will eventually have functions to calculate how much a card has gained or lost in value since purchase. For now, it's a placeholder as I figure out the best way to do these calculations.

Next steps:
- Decide on the formula for ROI (simple: (market_value - purchase_price) / purchase_price)
- Write a function that takes in purchase and market value and returns ROI
"""

# Placeholder function for ROI calculation
def calculate_roi(purchase_price, market_value):
    """
    Calculate the return on investment for a card.
    For now, just uses a simple formula. Will improve as I learn more.
    """
    if purchase_price == 0:
        return 0  # Avoid division by zero
    return (market_value - purchase_price) / purchase_price

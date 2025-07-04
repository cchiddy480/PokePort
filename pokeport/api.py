"""
api.py - Handles communication with the Pokemon TCG API.

Why this file exists:
> The Pokemon TCG API provides accurate card data (names, sets, rarities, images) that we can use to make sure users are adding the correct cards to their collection. This saves them from typos and ensures consistency. I'm learning how to work with external APIs and handle JSON responses.

Next steps:
- Add more search filters (rarity, card number)
- Cache results to avoid repeated API calls
- Handle API rate limits gracefully
"""

import requests
import json
import time
from typing import List, Dict, Optional

# API configuration
BASE_URL = "https://api.pokemontcg.io/v2"
API_KEY = "6ab60738-dc13-41ed-9aed-e24fedec7ea5"  # TODO: Move this to environment variables later

# Simple cache to avoid repeated API calls
# In a real app, you might use Redis or a database for this
_cache = {}
_cache_timeout = 300  # Cache results for 5 minutes

def _get_cached_data(key: str) -> Optional[List[Dict]]:
    """Get data from cache if it's still valid."""
    if key in _cache:
        data, timestamp = _cache[key]
        if time.time() - timestamp < _cache_timeout:
            return data
        else:
            del _cache[key]  # Remove expired cache entry
    return None

def _set_cached_data(key: str, data: List[Dict]) -> None:
    """Store data in cache with current timestamp."""
    _cache[key] = (data, time.time())

def search_cards_by_name(card_name: str) -> List[Dict]:
    """
    Search for Pokemon cards by name using the Pokemon TCG API.
    
    This function makes a request to the API to find all cards with the given name.
    Returns a list of card data dictionaries.
    
    Args:
        card_name (str): The name of the Pokemon card to search for
        
    Returns:
        List[Dict]: List of card data from the API
    """
    # Check cache first
    cache_key = f"search_{card_name.lower()}"
    cached_data = _get_cached_data(cache_key)
    if cached_data:
        print("📋 Using cached results...")
        return cached_data
    
    try:
        # Set up the API request headers
        headers = {
            "X-Api-Key": API_KEY,
            "Content-Type": "application/json"
        }
        
        # Build the search query
        params = {
            "q": f"name:{card_name}",
            "pageSize": 250  # Get more results to work with
        }
        
        print(f"🌐 Making API request for '{card_name}'...")
        # Make the API request
        response = requests.get(f"{BASE_URL}/cards", headers=headers, params=params, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the JSON response
        data = response.json()
        cards = data.get("data", [])
        
        # Cache the results
        _set_cached_data(cache_key, cards)
        
        return cards
        
    except requests.exceptions.Timeout:
        print("❌ API request timed out. Please try again.")
        return []
    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse API response: {e}")
        return []

def search_cards_advanced(card_name: str, set_name: str = "", card_number: str = "", rarity: str = "") -> List[Dict]:
    """
    Advanced search with multiple filters to narrow down results.
    
    This function builds a more specific search query to get fewer, more relevant results.
    
    Args:
        card_name (str): The name of the Pokemon card
        set_name (str): Optional set name filter
        card_number (str): Optional card number filter
        rarity (str): Optional rarity filter
        
    Returns:
        List[Dict]: Filtered list of card data
    """
    # Build cache key based on all search parameters
    cache_key = f"advanced_{card_name.lower()}_{set_name.lower()}_{card_number}_{rarity.lower()}"
    cached_data = _get_cached_data(cache_key)
    if cached_data:
        print("📋 Using cached results...")
        return cached_data
    
    try:
        headers = {
            "X-Api-Key": API_KEY,
            "Content-Type": "application/json"
        }
        
        # Build a more specific search query using correct API syntax
        query_parts = [f"name:\"{card_name}\""]
        if set_name:
            # Handle promo card searches better
            if "promo" in set_name.lower():
                # For promo searches, we'll do a broader search and filter later
                pass  # Don't add set filter for promo searches
            else:
                query_parts.append(f"set.name:\"{set_name}\"")
        if card_number:
            query_parts.append(f"number:\"{card_number}\"")
        if rarity:
            query_parts.append(f"rarity:\"{rarity}\"")
        
        query = " AND ".join(query_parts)
        
        params = {
            "q": query,
            "pageSize": 100  # Increased for promo searches
        }
        
        print(f"🌐 Making advanced API request...")
        response = requests.get(f"{BASE_URL}/cards", headers=headers, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        cards = data.get("data", [])
        
        # If searching for promos, filter the results
        if set_name and "promo" in set_name.lower():
            promo_cards = []
            for card in cards:
                card_set_name = card.get("set", {}).get("name", "").lower()
                if "promo" in card_set_name or "black star" in card_set_name:
                    promo_cards.append(card)
            cards = promo_cards
        
        # Cache the results
        _set_cached_data(cache_key, cards)
        
        return cards
        
    except requests.exceptions.Timeout:
        print("❌ API request timed out. Please try again.")
        return []
    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse API response: {e}")
        return []

def get_promo_sets_for_cards(cards: List[Dict]) -> List[str]:
    """
    Extract promo set names from a list of cards.
    
    This helps users find promo cards specifically.
    
    Args:
        cards (List[Dict]): List of card data from the API
        
    Returns:
        List[str]: List of promo set names
    """
    promo_sets = set()
    for card in cards:
        set_name = card.get("set", {}).get("name", "")
        if "promo" in set_name.lower() or "black star" in set_name.lower():
            promo_sets.add(set_name)
    return sorted(list(promo_sets))

def suggest_promo_search(card_name: str) -> List[Dict]:
    """
    Suggest promo cards for a given Pokemon name.
    
    This function specifically searches for promo cards and provides helpful guidance.
    
    Args:
        card_name (str): The name of the Pokemon card
        
    Returns:
        List[Dict]: List of promo card data
    """
    print(f"🔍 Searching for {card_name} promo cards...")
    
    # Search for all cards first
    all_cards = search_cards_by_name(card_name)
    
    # Filter for promo cards
    promo_cards = []
    for card in all_cards:
        set_name = card.get("set", {}).get("name", "").lower()
        if "promo" in set_name or "black star" in set_name:
            promo_cards.append(card)
    
    if promo_cards:
        print(f"✅ Found {len(promo_cards)} promo cards for {card_name}")
        promo_sets = get_promo_sets_for_cards(promo_cards)
        print(f"📋 Promo sets available: {', '.join(promo_sets)}")
    else:
        print(f"❌ No promo cards found for {card_name}")
    
    return promo_cards

def get_sets_for_cards(cards: List[Dict]) -> List[str]:
    """
    Extract unique set names from a list of cards.
    
    This helps us show users what sets are available for filtering.
    
    Args:
        cards (List[Dict]): List of card data from the API
        
    Returns:
        List[str]: List of unique set names
    """
    sets = set()
    for card in cards:
        set_name = card.get("set", {}).get("name", "Unknown Set")
        sets.add(set_name)
    return sorted(list(sets))

def filter_cards_by_set(cards: List[Dict], set_name: str) -> List[Dict]:
    """
    Filter a list of cards to only include cards from a specific set.
    
    Args:
        cards (List[Dict]): List of card data from the API
        set_name (str): The name of the set to filter by
        
    Returns:
        List[Dict]: Filtered list of cards from the specified set
    """
    filtered_cards = []
    for card in cards:
        if card.get("set", {}).get("name") == set_name:
            filtered_cards.append(card)
    return filtered_cards

def filter_cards_by_rarity(cards: List[Dict], rarity: str) -> List[Dict]:
    """
    Filter a list of cards by rarity.
    
    Args:
        cards (List[Dict]): List of card data from the API
        rarity (str): The rarity to filter by
        
    Returns:
        List[Dict]: Filtered list of cards with the specified rarity
    """
    filtered_cards = []
    for card in cards:
        if card.get("rarity", "").lower() == rarity.lower():
            filtered_cards.append(card)
    return filtered_cards

def display_card_options(cards: List[Dict]) -> None:
    """
    Display a list of cards in a user-friendly format.
    
    Shows card name, set, and card number to help users identify the right card.
    
    Args:
        cards (List[Dict]): List of card data to display
    """
    if not cards:
        print("No cards found matching your criteria.")
        return
    
    print(f"\nFound {len(cards)} cards:")
    print("-" * 80)
    
    for i, card in enumerate(cards, 1):
        name = card.get("name", "Unknown")
        set_name = card.get("set", {}).get("name", "Unknown Set")
        card_number = card.get("number", "?")
        total_cards = card.get("set", {}).get("total", "?")
        rarity = card.get("rarity", "Unknown")
        
        print(f"{i}. {name} - {set_name} ({card_number}/{total_cards}) - {rarity}")
    
    print("-" * 80)

def get_card_details(card: Dict) -> Dict:
    """
    Extract the important details from a card API response.
    
    Converts the API response into a format that matches our PokemonCard model.
    
    Args:
        card (Dict): Card data from the API
        
    Returns:
        Dict: Simplified card details
    """
    return {
        "name": card.get("name", ""),
        "set_name": card.get("set", {}).get("name", ""),
        "rarity": card.get("rarity", ""),
        "image_url": card.get("images", {}).get("small", ""),
        "card_number": card.get("number", ""),
        "total_cards": card.get("set", {}).get("total", "")
    }

def clear_cache() -> None:
    """Clear the API cache. Useful for testing or when cache gets too large."""
    global _cache
    _cache.clear()
    print("🗑️ Cache cleared.")

# Example usage and testing
if __name__ == "__main__":
    # Test the API integration
    print("Testing Pokemon TCG API integration...")
    
    # Test basic search
    cards = search_cards_by_name("Pikachu")
    print(f"Found {len(cards)} Pikachu cards")
    
    if cards:
        sets = get_sets_for_cards(cards)
        print(f"Available sets: {sets[:5]}...")  # Show first 5 sets
        
        # Test advanced search
        print("\nTesting advanced search...")
        advanced_cards = search_cards_advanced("Pikachu", set_name="Base Set")
        print(f"Found {len(advanced_cards)} Pikachu cards in Base Set") 
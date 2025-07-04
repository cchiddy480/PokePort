"""
cli.py - The command-line interface for PokePort.

Why this file exists:
> This is where users will interact with the app from the terminal. For now, it just initializes the database so I can check that everything is wired up correctly. As I learn more, I'll add commands for adding, viewing, and managing cards.
"""

from pokeport.storage import init_db, add_card, get_all_cards
from pokeport.models import PokemonCard
from pokeport.grading import estimate_psa_grade
from pokeport.api import search_cards_by_name, search_cards_advanced, get_sets_for_cards, filter_cards_by_set, filter_cards_by_rarity, display_card_options, get_card_details, suggest_promo_search, get_promo_sets_for_cards

# Initialize the database when running this script.
# This is a good first test to make sure the DB setup works!
init_db()

# --- Simple CLI Menu for Card Management and Grading ---
def main_menu():
    print("\nWelcome to PokePort CLI!")
    print("Manage your Pokemon card collection and estimate grades.")
    print("(More features coming as I learn and build them!)\n")
    while True:
        print("Menu:")
        print("1. Add a new card to collection (with API search)")
        print("2. Add a new card manually")
        print("3. View all cards in collection")
        print("4. Estimate a card's grade (PSA style)")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            run_add_card_with_api()
        elif choice == "2":
            run_add_card_manual()
        elif choice == "3":
            run_view_cards()
        elif choice == "4":
            run_grading_estimator()
        elif choice == "0":
            print("Goodbye! (Back to building more features soon)")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 0.")

def run_add_card_with_api():
    """Add a new Pokemon card using API search for accurate data."""
    print("\n--- Add New Card (API Search) ---")
    print("Let's find your card using the Pokemon TCG database!")
    print("The more details you provide, the faster we can find your card.\n")
    
    try:
        # Step 1: Get basic card information with optional filters
        card_name = input("Enter the Pokemon card name (e.g., Pikachu): ").strip()
        if not card_name:
            print("❌ Card name is required.")
            return
        
        # Optional filters to narrow down results
        print("\nOptional filters (press Enter to skip):")
        set_name = input("Set name (e.g., Base Set, Jungle, or 'promo' for promo cards): ").strip()
        card_number = input("Card number (e.g., 58, 58/102): ").strip()
        rarity = input("Rarity (e.g., Common, Uncommon, Rare): ").strip()
        
        # Special handling for promo cards
        if set_name and "promo" in set_name.lower():
            print("\n💡 Searching for promo cards...")
            print("💡 Promo cards are often in sets like 'BW Black Star Promos', 'DP Black Star Promos', etc.")
            cards = suggest_promo_search(card_name)
            if not cards:
                print("💡 Try searching without the 'promo' filter to see all available sets first.")
                return
        else:
            # Step 2: Use advanced search if filters are provided, otherwise basic search
            if set_name or card_number or rarity:
                print(f"\n🔍 Making advanced search for '{card_name}'...")
                cards = search_cards_advanced(card_name, set_name, card_number, rarity)
            else:
                print(f"\n🔍 Searching for '{card_name}' cards...")
                cards = search_cards_by_name(card_name)
        
        if not cards:
            print(f"❌ No cards found for '{card_name}' with the given filters.")
            print("💡 Try removing some filters or use manual entry.")
            return
        
        # Step 3: If we still have too many results, help user narrow down
        if len(cards) > 10:
            print(f"\n⚠️ Found {len(cards)} cards. Let's narrow this down:")
            
            # Show available sets
            sets = get_sets_for_cards(cards)
            print(f"\nAvailable sets ({len(sets)} total):")
            for i, set_name_option in enumerate(sets[:10], 1):  # Show first 10 sets
                print(f"{i}. {set_name_option}")
            if len(sets) > 10:
                print(f"... and {len(sets) - 10} more sets")
            
            # Let user choose a set
            set_choice = input(f"\nChoose a set (1-{min(10, len(sets))}) or press Enter to see all: ").strip()
            if set_choice:
                try:
                    set_index = int(set_choice) - 1
                    if 0 <= set_index < len(sets):
                        selected_set = sets[set_index]
                        cards = filter_cards_by_set(cards, selected_set)
                        print(f"✅ Filtered to {len(cards)} cards from {selected_set}")
                    else:
                        print("❌ Invalid set choice.")
                        return
                except ValueError:
                    print("❌ Please enter a valid number.")
                    return
        
        # Step 4: Display final card options
        display_card_options(cards)
        
        # Step 5: Let user choose the specific card
        if len(cards) == 1:
            print("\n✅ Only one card found - automatically selected!")
            selected_card = cards[0]
        else:
            card_choice = input(f"\nChoose a card (1-{len(cards)}): ").strip()
            try:
                card_index = int(card_choice) - 1
                if card_index < 0 or card_index >= len(cards):
                    print("❌ Invalid card choice.")
                    return
                selected_card = cards[card_index]
            except ValueError:
                print("❌ Please enter a valid number.")
                return
        
        # Step 6: Get card details and additional info
        card_details = get_card_details(selected_card)
        print(f"\n✅ Selected: {card_details['name']} - {card_details['set_name']} ({card_details['card_number']}/{card_details['total_cards']}) - {card_details['rarity']}")
        
        # Get price information
        purchase_price = float(input("Purchase price ($): "))
        market_value = float(input("Current market value ($): "))
        
        # Get grading scores
        print("\nNow let's grade the card condition (1-10 scale):")
        centering = int(input("Centering (1-10): "))
        corners = int(input("Corners (1-10): "))
        edges = int(input("Edges (1-10): "))
        surface = int(input("Surface (1-10): "))
        
        # Calculate the grading score
        grading_score, _ = estimate_psa_grade(centering, corners, edges, surface)
        
        # Create the PokemonCard object with API data
        new_card = PokemonCard(
            name=card_details['name'],
            set_name=card_details['set_name'],
            rarity=card_details['rarity'],
            purchase_price=purchase_price,
            market_value=market_value,
            grading_score=grading_score,
            image_url=card_details['image_url']
        )
        
        # Save to database
        card_id = add_card(new_card)
        print(f"\n✅ Card added successfully! (ID: {card_id})")
        print(f"Estimated Grade: {grading_score:.2f}")
        
    except ValueError as e:
        print(f"❌ Error: Please enter valid numbers for prices and grading scores.")
    except Exception as e:
        print(f"❌ Error adding card: {e}")
    
    print("---\n")

def run_add_card_manual():
    """Add a new Pokemon card to the collection (manual entry)."""
    print("\n--- Add New Card (Manual Entry) ---")
    print("Enter card details manually:")
    
    try:
        # Get basic card information
        name = input("Card name (e.g., Pikachu): ").strip()
        set_name = input("Set name (e.g., Base Set): ").strip()
        rarity = input("Rarity (e.g., Common, Uncommon, Rare): ").strip()
        
        # Get price information
        purchase_price = float(input("Purchase price ($): "))
        market_value = float(input("Current market value ($): "))
        
        # Get grading scores
        print("\nNow let's grade the card condition (1-10 scale):")
        centering = int(input("Centering (1-10): "))
        corners = int(input("Corners (1-10): "))
        edges = int(input("Edges (1-10): "))
        surface = int(input("Surface (1-10): "))
        
        # Calculate the grading score
        grading_score, _ = estimate_psa_grade(centering, corners, edges, surface)
        
        # Optional image URL
        image_url = input("Image URL (optional, press Enter to skip): ").strip()
        if not image_url:
            image_url = None
        
        # Create the PokemonCard object
        new_card = PokemonCard(
            name=name,
            set_name=set_name,
            rarity=rarity,
            purchase_price=purchase_price,
            market_value=market_value,
            grading_score=grading_score,
            image_url=image_url
        )
        
        # Save to database
        card_id = add_card(new_card)
        print(f"\n✅ Card added successfully! (ID: {card_id})")
        print(f"Estimated Grade: {grading_score:.2f}")
        
    except ValueError as e:
        print(f"❌ Error: Please enter valid numbers for prices and grading scores.")
    except Exception as e:
        print(f"❌ Error adding card: {e}")
    
    print("---\n")

def run_view_cards():
    """Display all cards in the collection."""
    print("\n--- Your Card Collection ---")
    
    try:
        cards = get_all_cards()
        if not cards:
            print("No cards in your collection yet. Add some cards first!")
        else:
            print(f"Total cards: {len(cards)}")
            print("-" * 60)
            for card in cards:
                print(f"ID: {card.id}")
                print(f"Name: {card.name}")
                print(f"Set: {card.set_name}")
                print(f"Rarity: {card.rarity}")
                print(f"Purchase: ${card.purchase_price:.2f}")
                print(f"Market Value: ${card.market_value:.2f}")
                print(f"Grade: {card.grading_score:.2f}")
                print("-" * 60)
    except Exception as e:
        print(f"❌ Error loading cards: {e}")
    
    print("---\n")

def run_grading_estimator():
    print("\n--- PSA Grading Estimator ---")
    print("Enter a score from 1 (poor) to 10 (gem mint) for each category.")
    try:
        centering = int(input("Centering (1-10): "))
        corners = int(input("Corners (1-10): "))
        edges = int(input("Edges (1-10): "))
        surface = int(input("Surface (1-10): "))
    except ValueError:
        print("Oops! Please enter whole numbers between 1 and 10.")
        return
    # Call the grading estimator
    grade, explanation = estimate_psa_grade(centering, corners, edges, surface)
    print(f"\nEstimated Grade: {grade:.2f}")
    print(explanation)
    print("---\n")

if __name__ == "__main__":
    main_menu()

"""
cli.py - The command-line interface for PokePort.

Why this file exists:
> This is where users will interact with the app from the terminal. For now, it just initializes the database so I can check that everything is wired up correctly. As I learn more, I'll add commands for adding, viewing, and managing cards.
"""

from pokeport.storage import init_db, add_card, get_all_cards
from pokeport.models import PokemonCard
from pokeport.grading import estimate_psa_grade

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
        print("1. Add a new card to collection")
        print("2. View all cards in collection")
        print("3. Estimate a card's grade (PSA style)")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            run_add_card()
        elif choice == "2":
            run_view_cards()
        elif choice == "3":
            run_grading_estimator()
        elif choice == "0":
            print("Goodbye! (Back to building more features soon)")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 0.")

def run_add_card():
    """Add a new Pokemon card to the collection."""
    print("\n--- Add New Card ---")
    print("Let's add a new Pokemon card to your collection!")
    
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

"""
cli.py - The command-line interface for PokePort.

Why this file exists:
> This is where users will interact with the app from the terminal. For now, it just initializes the database so I can check that everything is wired up correctly. As I learn more, I'll add commands for adding, viewing, and managing cards.
"""

from pokeport.storage import init_db
from pokeport.grading import estimate_psa_grade

# Initialize the database when running this script.
# This is a good first test to make sure the DB setup works!
init_db()

# --- Simple CLI Menu for Grading Estimator ---
def main_menu():
    print("\nWelcome to PokePort CLI!")
    print("This is a super basic menu to demo the grading estimator.")
    print("(More features coming as I learn and build them!)\n")
    while True:
        print("Menu:")
        print("1. Estimate a card's grade (PSA style)")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            run_grading_estimator()
        elif choice == "0":
            print("Goodbye! (Back to building more features soon)")
            break
        else:
            print("Invalid choice. Please enter 1 or 0.")

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

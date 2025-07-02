"""
cli.py - The command-line interface for PokePort.

Why this file exists:
> This is where users will interact with the app from the terminal. For now, it just initializes the database so I can check that everything is wired up correctly. As I learn more, I'll add commands for adding, viewing, and managing cards.
"""

from pokeport.storage import init_db

# Initialize the database when running this script.
# This is a good first test to make sure the DB setup works!
init_db()

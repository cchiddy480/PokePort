# This module handles the database operations for storing and retrieving Pokémon card data.
import sqlite3

# Database configuration
DB_NAME = 'pokemon_card_data.db'

# Function to initialize the database and create the necessary tables
def init_db():
    # Initialize the database and create the pokemon table if it doesn't exist
    with sqlite3.connect(DB_NAME) as connection:
        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()
        # Create the pokemon table with the specified columns
        cursor.execute(''' 
                       CREATE TABLE IF NOT EXISTS pokemon (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       set TEXT NOT NULL,
                       rarity TEXT NOT NULL,
                       purchase_price REAL,
                       market_value REAL,
                       grading_score REAL,
                       image_url TEXT) ''')
        
        print("Database initialized and table created.")


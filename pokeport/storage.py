# This module handles the database operations for storing and retrieving Pokémon card data.
# This file handles saving and loading Pokemon card data using a SQLite database.
# It provides functions to add, get, update, and delete cards in the database.

import sqlite3
from pokeport.models import PokemonCard
from typing import List, Optional

# The name of the database file where card data is stored
DB_NAME = 'pokemon_card_data.db'

# This function creates the database and the table for storing Pokemon cards if they don't exist yet.
def init_db():
    # Connect to the database file (it will be created if it doesn't exist)
    with sqlite3.connect(DB_NAME) as connection:
        # Create a cursor to run SQL commands
        cursor = connection.cursor()
        # Create the table for storing Pokemon cards
        cursor.execute(''' 
                       CREATE TABLE IF NOT EXISTS pokemon (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       set_name TEXT NOT NULL,
                       rarity TEXT NOT NULL,
                       purchase_price REAL,
                       market_value REAL,
                       grading_score REAL,
                       image_url TEXT) ''')
        # Print a message to show the database is ready
        print("Database initialized and table created.")

# This function adds a new Pokemon card to the database.
# It returns the ID of the new card.
def add_card(card: PokemonCard) -> int:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        # Insert the card data into the table
        cursor.execute('''
            INSERT INTO pokemon (name, set_name, rarity, purchase_price, market_value, grading_score, image_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (card.name, card.set_name, card.rarity, card.purchase_price, card.market_value, card.grading_score, card.image_url))
        connection.commit()
        # Get the ID of the new card
        if cursor.lastrowid is None:
            raise RuntimeError("Failed to insert card and retrieve lastrowid.")
        return cursor.lastrowid

# This function gets a single Pokemon card from the database by its ID.
# It returns a PokemonCard object, or None if the card is not found.
def get_card(card_id: int) -> Optional[PokemonCard]:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        # Select the card with the given ID
        cursor.execute('SELECT * FROM pokemon WHERE id = ?', (card_id,))
        row = cursor.fetchone()
        if row:
            # Create a PokemonCard object from the row data
            return PokemonCard(
                id=row[0], name=row[1], set_name=row[2], rarity=row[3],
                purchase_price=row[4], market_value=row[5], grading_score=row[6], image_url=row[7]
            )
        return None

# This function gets all Pokemon cards from the database.
# It returns a list of PokemonCard objects.
def get_all_cards() -> List[PokemonCard]:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        # Select all cards from the table
        cursor.execute('SELECT * FROM pokemon')
        rows = cursor.fetchall()
        # Create a list of PokemonCard objects from the rows
        return [
            PokemonCard(
                id=row[0], name=row[1], set_name=row[2], rarity=row[3],
                purchase_price=row[4], market_value=row[5], grading_score=row[6], image_url=row[7]
            ) for row in rows
        ]

# This function updates an existing Pokemon card in the database.
# The card must have an ID.
def update_card(card: PokemonCard) -> None:
    if card.id is None:
        raise ValueError("Card must have an id to be updated.")
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        # Update the card data in the table
        cursor.execute('''
            UPDATE pokemon SET name=?, set_name=?, rarity=?, purchase_price=?, market_value=?, grading_score=?, image_url=?
            WHERE id=?
        ''', (card.name, card.set_name, card.rarity, card.purchase_price, card.market_value, card.grading_score, card.image_url, card.id))
        connection.commit()

# This function deletes a Pokemon card from the database by its ID.
def delete_card(card_id: int) -> None:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        # Delete the card with the given ID
        cursor.execute('DELETE FROM pokemon WHERE id=?', (card_id,))
        connection.commit()




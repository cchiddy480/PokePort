# This module handles the database operations for storing and retrieving Pokémon card data.
import sqlite3
from pokeport.models import PokemonCard
from typing import List, Optional

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
                       set_name TEXT NOT NULL,
                       rarity TEXT NOT NULL,
                       purchase_price REAL,
                       market_value REAL,
                       grading_score REAL,
                       image_url TEXT) ''')
        
        print("Database initialized and table created.")

def add_card(card: PokemonCard) -> int:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO pokemon (name, set_name, rarity, purchase_price, market_value, grading_score, image_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (card.name, card.set_name, card.rarity, card.purchase_price, card.market_value, card.grading_score, card.image_url))
        connection.commit()
        if cursor.lastrowid is None:
            raise RuntimeError("Failed to insert card and retrieve lastrowid.")
        return cursor.lastrowid

def get_card(card_id: int) -> Optional[PokemonCard]:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM pokemon WHERE id = ?', (card_id,))
        row = cursor.fetchone()
        if row:
            return PokemonCard(
                id=row[0], name=row[1], set_name=row[2], rarity=row[3],
                purchase_price=row[4], market_value=row[5], grading_score=row[6], image_url=row[7]
            )
        return None

def get_all_cards() -> List[PokemonCard]:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM pokemon')
        rows = cursor.fetchall()
        return [
            PokemonCard(
                id=row[0], name=row[1], set_name=row[2], rarity=row[3],
                purchase_price=row[4], market_value=row[5], grading_score=row[6], image_url=row[7]
            ) for row in rows
        ]

def update_card(card: PokemonCard) -> None:
    if card.id is None:
        raise ValueError("Card must have an id to be updated.")
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE pokemon SET name=?, set_name=?, rarity=?, purchase_price=?, market_value=?, grading_score=?, image_url=?
            WHERE id=?
        ''', (card.name, card.set_name, card.rarity, card.purchase_price, card.market_value, card.grading_score, card.image_url, card.id))
        connection.commit()

def delete_card(card_id: int) -> None:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM pokemon WHERE id=?', (card_id,))
        connection.commit()




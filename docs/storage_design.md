# Storage Design – PokePort

## Storage Format: SQLite

**Why SQLite?**
- Lightweight and file-based — no server setup required
- Real relational database experience (SQL syntax, schemas, etc.)
- Supports querying, sorting, filtering — critical for analytics
- Scalable enough for a small-to-medium personal collection

Alternative considered: JSON  
**Rejected due to** lack of querying support and lower data integrity.

---

## Card Table Schema

| Column           | Type     | Description |
|------------------|----------|-------------|
| `id`             | INTEGER  | Auto-incrementing primary key |
| `name`           | TEXT     | Name of the Pokémon card |
| `set`            | TEXT     | The set the card belongs to (e.g., "Base Set") |
| `rarity`         | TEXT     | Card rarity (e.g., "Rare Holo") |
| `purchase_price` | REAL     | Amount paid by user |
| `market_value`   | REAL     | Estimated current market value |
| `grading_score`  | REAL     | Placeholder for future grading mechanic |
| `image_url`      | TEXT     | Future GUI use — shows image from web or local path |

---

## Notes on Expansion

- Optional future fields:
  - `notes`, `date_added`, `is_graded`, `grader`
- Current CLI features will support:
  - Add, View, Update, Delete
  - Summary insights (e.g., value tracking, profit/loss)
- GUI planned — `image_url` included as prep


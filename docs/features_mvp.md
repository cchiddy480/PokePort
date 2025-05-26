# ✅ MVP Features: PokePort

This document outlines the **Minimum Viable Product (MVP)** feature set for PokePort. These are the essential features required for the application to function as a useful tool for collectors and investors. All other features are considered stretch goals and are documented separately in `project_scope.md`.

---

## 📦 1. Local Collection Manager

**Core Functionality:**
- [ ] Add new cards to the collection
- [ ] Edit existing card details
- [ ] Remove cards from the collection
- [ ] Store and retrieve collection data using local JSON file

**Minimum Card Fields:**
- Card name
- Set
- Purchase price
- Condition (text description)
- Purchase date (optional)
- Notes (optional)

---

## 📈 2. Value & ROI Tracking

**Core Functionality:**
- [ ] Manually input current market value for each card
- [ ] Automatically calculate:
  - Profit/Loss per card
  - ROI (%) = ((Current Value - Purchase Price) / Purchase Price) × 100
  - Total invested value vs current collection value
- [ ] Provide a summary view of portfolio stats

---

## 🧪 3. Manual Grading Estimator

**Core Functionality:**
- [ ] Prompt user to input values for:
  - Centering (Y/N)
  - Whitening (Y/N)
  - Scratches (Y/N)
  - Corners (Y/N)
- [ ] Run logic tree to estimate potential grade (e.g., "Estimated PSA 8–9")
- [ ] Show basic grading advice based on inputs

---

## 🖥 4. Interface (CLI or Streamlit)

**Core Functionality:**
- [ ] View full card collection
- [ ] Filter/search by set, value, grade, etc.
- [ ] Add/edit/remove cards from the collection
- [ ] View grading estimates and portfolio summary
- [ ] Basic UI feedback (e.g., green for gains, red for losses)

---

## 🧪 5. Basic Test Coverage

**Core Functionality:**
- [ ] Unit tests for ROI calculator and grading logic
- [ ] Use test JSON data to validate collection manager functions

---

## 🔗 Reference
For stretch goals and future planning, see `project_scope.md`.

---

This MVP scope defines the baseline product for PokePort. Upon completion, the tool should allow users to manage a card collection, calculate ROI, and estimate grades — all from a local, free, and user-friendly interface.

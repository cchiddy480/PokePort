## User Story Definition & Planning 
### Goal:
> Develop clear user stories that define the core functionality of the **Collection Manager**, which allows users to manage their Pokémon card investments.

## User Stories 
| ID  | User Story | Feature(s) | Priority |
|-----|------------|------------|----------|
| US1 | As a user, I want to **add a new Pokémon card** to my collection so I can track my purchases. | `add_card()` |  High |
| US2 | As a user, I want to **view all cards in my collection**, including price and grade, so I can see what I own. | `view_cards()` |  Medium |
| US3 | As a user, I want to **update the details** of a card (e.g., price, grade) so that I can reflect new grading results or corrected info. | `update_card()` |  Medium |
| US4 | As a user, I want to **delete cards** I no longer own or added by mistake so my collection stays accurate. | `delete_card()` |  Medium |
| US5 | As a user, I want to **see a summary of total spend, estimated value, and profit/loss** so I can track my investment. | `get_summary()` |  Low |
| US6 | As a user, I want the system to **warn me if I try to add a duplicate card** (same name and purchase date), to avoid accidental entries. | `add_card()` with validation |  Medium |

## Edge Cases to Handle
| Scenario                                              | Affected Feature              | Handling Strategy                      |
| ----------------------------------------------------- | ----------------------------- | -------------------------------------- |
| Duplicate card entry (e.g. same name + purchase date) | `add_card()`                  | Check for existing entry; prompt user  |
| Missing required fields (e.g. price, name)            | `add_card()`, `update_card()` | Validate input before saving           |
| Invalid input types (e.g. price as text)              | `add_card()`, `update_card()` | Type checking and error messaging      |
| Deleting a card that doesn't exist                    | `delete_card()`               | Graceful error or "not found" message  |
| Viewing when no cards exist                           | `view_cards()`                | Return a helpful message, not an error |
| Summary with missing price/values                     | `get_summary()`               | Skip or default nulls to zero          |



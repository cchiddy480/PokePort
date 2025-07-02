"""
grading.py - Handles the logic for estimating the grading of a Pokémon card.

Why this file exists:
> Grading is a big part of the Pokémon card world. This module contains functions to help estimate what grade a card might get based on its condition. For now, I'm using the main PSA grading criteria: centering, corners, edges, and surface. This is a simple version to get started and help me learn how grading works in practice.

Next steps:
- Improve the grading logic as I learn more about how PSA (and others) actually weight each category.
- Maybe add more detailed feedback or suggestions for improving card condition.
"""

def estimate_psa_grade(centering, corners, edges, surface):
    """
    Estimate a PSA-style grade for a Pokémon card.

    PSA uses four main criteria:
    - Centering
    - Corners
    - Edges
    - Surface

    Each should be a score from 1 (poor) to 10 (gem mint).
    This function just averages the four scores for now.

    Returns:
        grade (float): The estimated grade (1-10 scale)
        explanation (str): A short explanation of how the grade was calculated
    """
    # Collect the scores in a list for easy averaging
    scores = [centering, corners, edges, surface]
    # Calculate the average score
    grade = sum(scores) / len(scores)
    # Build an explanation string
    explanation = (
        f"Grading breakdown: Centering={centering}, Corners={corners}, Edges={edges}, Surface={surface}.\n"
        f"Estimated grade is the average of these scores: {grade:.2f} (out of 10).\n"
        "Note: This is a simple average. Real PSA grading may weight categories differently and include more nuance."
    )
    return grade, explanation

# Example usage (for testing/learning):
if __name__ == "__main__":
    # Example: all categories are near mint
    grade, explanation = estimate_psa_grade(9, 9, 8, 9)
    print(f"Estimated Grade: {grade:.2f}")
    print(explanation)

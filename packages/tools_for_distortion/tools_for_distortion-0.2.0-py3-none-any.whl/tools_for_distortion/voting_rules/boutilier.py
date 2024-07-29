# src/voting_rules/boutilier.py

import random
from src.voting_rules.harmonic import harmonic_scoring_rule
from src.utils.validators import validate_ranking_data

def boutilier_random_harmonic(ranking_data, num_alternatives):
    """
    Chooses an alternative based on a combination of random selection and harmonic scoring.

    Args:
        ranking_data (list): A list of tuples containing ranking information.
        num_alternatives (int): The number of alternatives.

    Returns:
        int: The identifier of the selected alternative.
    """
    # Validate inputs
    validate_ranking_data(ranking_data, num_alternatives)  # Validate ranking data

    # Choose an alternative
    if random.random() < 0.5:
        # Select uniformly at random
        selected_alternative = random.randint(1, num_alternatives)
    else:
        # Select based on harmonic scores
        normalized_scores = harmonic_scoring_rule(ranking_data, num_alternatives, randomised=True)
        # Make two lists from the dictionary normalized_scores
        candidates, probabilities = zip(*normalized_scores.items())
        # Select one candidate from the list candidates, with the probabilities from the list probabilities
        selected_alternative = random.choices(candidates, weights=probabilities, k=1)[0]

    return selected_alternative

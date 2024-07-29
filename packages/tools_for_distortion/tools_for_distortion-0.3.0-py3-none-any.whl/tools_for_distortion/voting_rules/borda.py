# src/voting_rules/borda.py

from src.tools_for_distortion.utils.scoring_rules import apply_scoring_rule
from src.tools_for_distortion.utils.validators import validate_ranking_data, validate_scoring_vector

def borda_scoring_rule(ranking_data, num_alternatives, randomised=False):
    """
    Calculates the scores of candidates using the Borda count scoring rule.

    In Borda count, each position on a ballot is assigned a point value, with higher positions 
    receiving more points. The scores for each candidate are summed across all ballots.

    Args:
        ranking_data (list): A list of tuples, each containing the number of voters for a specific ranking and the ranking itself.
        num_alternatives (int): The number of alternatives.
        randomised (bool): A flag indicating whether to return normalized scores or the highest-scoring candidate.

    Returns:
        dict or tuple: Depending on the value of 'randomised':
        - If True: Returns a dictionary of normalized scores.
        - If False: Returns a tuple containing the highest-scoring candidate and their score.
    """
    # Validate inputs
    validate_ranking_data(ranking_data, num_alternatives)  # Validate ranking data
    scoring_vector = list(range(num_alternatives - 1, -1, -1))
    validate_scoring_vector(scoring_vector, num_alternatives)  # Validate scoring vector

    return apply_scoring_rule(ranking_data, num_alternatives, scoring_vector, randomised)

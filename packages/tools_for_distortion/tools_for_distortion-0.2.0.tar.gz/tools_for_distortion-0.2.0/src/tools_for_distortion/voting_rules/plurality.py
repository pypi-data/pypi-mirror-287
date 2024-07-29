from src.utils.scoring_rules import apply_scoring_rule
from src.utils.validators import validate_ranking_data, validate_scoring_vector


def plurality_scoring_rule(ranking_data, num_alternatives, randomised=False):
    """
    Calculates the scores of candidates using the plurality scoring rule.

    Args:
        ranking_data (list): A list of tuples, each containing the number of voters for a specific ranking and the ranking itself.
        num_alternatives: number of alternatives
        randomised (bool): A flag indicating whether to return normalized scores or the highest-scoring candidate.

    Returns:
        Depending on the value of 'randomised':
        - If True: Returns a dictionary of normalized scores.
        - If False: Returns a tuple containing the highest-scoring candidate and their score.
    """
    validate_ranking_data(ranking_data, num_alternatives)
    scoring_vector = [1] + [0] * (num_alternatives - 1)
    validate_scoring_vector(scoring_vector, num_alternatives)
    return apply_scoring_rule(ranking_data, num_alternatives, scoring_vector, randomised)

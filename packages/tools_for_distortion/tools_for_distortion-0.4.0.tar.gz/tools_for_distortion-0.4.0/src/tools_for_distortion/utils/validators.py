def validate_ranking_data(ranking_data, num_alternatives):
    """
    Validates the ranking data to ensure it meets the expected format and values.

    Args:
        ranking_data (list): A list of tuples containing ranking information.
        num_alternatives (int): Number of alternatives.

    Raises:
        ValueError: If the ranking data is not in the expected format or contains invalid values.
    """
    if not isinstance(ranking_data, list):
        raise ValueError("Ranking data must be a list of tuples.")
    
    for num_voters, ranks in ranking_data:
        if not isinstance(num_voters, int) or num_voters <= 0:
            raise ValueError(f"Number of voters must be a positive integer. Found: {num_voters}")
        if not isinstance(ranks, list) or len(ranks) != num_alternatives:
            raise ValueError(f"Ranks must be a list with {num_alternatives} elements. Found: {ranks}")
        if not all(isinstance(rank, int) and 1 <= rank <= num_alternatives for rank in ranks):
            raise ValueError(f"All ranks must be integers between 1 and {num_alternatives}. Found: {ranks}")

def validate_scoring_vector(scoring_vector, num_alternatives):
    """
    Validates the scoring vector to ensure it matches the number of alternatives.

    Args:
        scoring_vector (list): A list of scores for ranking positions.
        num_alternatives (int): Number of alternatives.

    Raises:
        ValueError: If the scoring vector does not match the number of alternatives.
    """
    if not isinstance(scoring_vector, list) or len(scoring_vector) != num_alternatives:
        raise ValueError(f"Scoring vector must be a list with {num_alternatives} elements. Found: {scoring_vector}")

def validate_probability_vector(probability_vector, num_alternatives):
    """
    Validates the probability vector to ensure it sums to 1 and matches the number of alternatives.

    Args:
        probability_vector (list): A list of probabilities for each candidate.
        num_alternatives (int): Number of alternatives.

    Raises:
        ValueError: If the probability vector does not sum to 1 or does not match the number of alternatives.
    """
    if not isinstance(probability_vector, list) or len(probability_vector) != num_alternatives:
        raise ValueError(f"Probability vector must be a list with {num_alternatives} elements. Found: {probability_vector}")
    if not all(isinstance(prob, (int, float)) and 0 <= prob <= 1 for prob in probability_vector):
        raise ValueError(f"All probabilities must be between 0 and 1. Found: {probability_vector}")
    if abs(sum(probability_vector) - 1.0) > 1e-6:
        raise ValueError(f"Probabilities must sum to 1. Sum found: {sum(probability_vector)}")

def validate_num_alternatives(num_alternatives):
    """
    Validates the number of alternatives to ensure it is a positive integer.

    Args:
        num_alternatives (int): Number of alternatives.

    Raises:
        ValueError: If the number of alternatives is not a positive integer.
    """
    if not isinstance(num_alternatives, int) or num_alternatives <= 0:
        raise ValueError(f"Number of alternatives must be a positive integer. Found: {num_alternatives}")

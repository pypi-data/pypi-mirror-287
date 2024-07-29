# returns a probability distribution over the candidates based on the scoring rule and total score
def normalized_scoring_vector(candidate_scores):
    """
    Normalizes the scores of candidates to form a probability distribution.

    Args:
        candidate_scores (dict): A dictionary with candidate identifiers as keys and their raw scores as values.

    Returns:
        dict: A dictionary with candidate identifiers as keys and their normalized scores as values.

    Raises:
        ValueError: If the total score is zero, making normalization impossible.
    """
    total_score = sum(candidate_scores.values())
    if total_score == 0:
        raise ValueError("Total score is zero, normalization not possible.")
    
    normalized_scores = {candidate: score / total_score for candidate, score in candidate_scores.items()}
    return normalized_scores
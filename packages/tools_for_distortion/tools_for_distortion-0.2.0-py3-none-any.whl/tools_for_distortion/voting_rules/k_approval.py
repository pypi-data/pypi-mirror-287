# src/voting_rules/k_approval.py

from src.utils.scoring_rules import scoring_rule
from src.utils.validators import validate_ranking_data, validate_scoring_vector

def k_approval_multi_winner(ranking_data, num_alternatives, k):
    """
    Implements the k-approval multi-winner scoring rule.

    Args:
        ranking_data (list): A list of tuples containing ranking information.
        num_alternatives (int): The number of alternatives.
        k (int): The number of top-ranked candidates to approve.

    Returns:
        tuple: A tuple containing the list of top 'k' candidates and their corresponding scores.
    """
    # Validate inputs
    validate_ranking_data(ranking_data, num_alternatives)  # Validate ranking data

    # Create a scoring vector for k-approval
    scoring_vector = [1 if i < k else 0 for i in range(num_alternatives)]
    validate_scoring_vector(scoring_vector, num_alternatives)  # Validate scoring vector

    # Calculate candidate scores
    candidate_scores = scoring_rule(ranking_data, scoring_vector, num_alternatives)

    # Sort candidates by score and select the top k
    top_candidates = sorted(candidate_scores, key=candidate_scores.get, reverse=True)[:k]
    top_scores = {candidate: candidate_scores[candidate] for candidate in top_candidates}

    return top_candidates, top_scores

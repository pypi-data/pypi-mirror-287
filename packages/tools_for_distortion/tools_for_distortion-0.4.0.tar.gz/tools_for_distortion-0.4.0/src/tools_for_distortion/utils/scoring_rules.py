from .normalization import normalized_scoring_vector


def scoring_rule(ranking_data, scoring_vector, num_alternatives):
    """
    Calculates the scores of candidates based on the provided scoring rule.

    Args:
        ranking_data (list): A list of tuples, each containing the number of voters for a specific ranking and the ranking itself.
        scoring_vector (list): A list of scores corresponding to each rank in the ranking.
        num_alternatives: number of alternatives

    Returns:
        dict: A dictionary with candidate identifiers as keys and their calculated scores as values.
    """
    # Initialize candidate scores for alternatives, starting from 0
    candidate_scores = {i: 0 for i in range(1, num_alternatives + 1)}
 
    # Process each voter's ranking
    for num_voters, ranks in ranking_data:
        # Iterate over each candidate's rank in the sequence
        for rank_index, candidate in enumerate(ranks):
            # Ensure the rank index is within the length of the scoring vector
            if rank_index < len(scoring_vector):
                # Add the score to the candidate times the number of voters with this ranking
                candidate_scores[candidate] += scoring_vector[rank_index] * num_voters
    
    

    return candidate_scores

# checks the flag for randomised scoring and applies the scoring rule
def apply_scoring_rule(ranking_data, num_alternatives, scoring_vector, randomised):
    
    """
    Applies a scoring rule to ranking data and returns the results, either as normalized scores or as the highest-scoring candidate.

    Args:
        ranking_data (list): A list of tuples containing ranking information.
        num_alternatives: number of alternatives
        scoring_vector (list): A list of scores for ranking positions.
        randomised (bool): A flag indicating whether to use normalized scoring.

    Returns:
        Depending on the value of 'randomised':
        - If True: Returns a dictionary of normalized scores.
        - If False: Returns a tuple containing the highest-scoring candidate and their score.
    """
    
    candidate_scores = scoring_rule(ranking_data, scoring_vector, num_alternatives)
    if randomised:
        return normalized_scoring_vector(candidate_scores)
    else:
        max_score_candidate = max(candidate_scores, key=candidate_scores.get)
        return max_score_candidate, candidate_scores[max_score_candidate]
from src.utils.validators import validate_ranking_data, validate_num_alternatives

def instant_runoff_voting(ranking_data, num_alternatives):
    """
    Implements the Instant Runoff Voting (IRV) electoral system.

    Args:
        ranking_data (list): A list of tuples containing ranking information.
        num_alternatives: Number of alternatives.

    Returns:
        The winning candidate identifier, or a list of candidates in the event of a tie.
    """
    validate_ranking_data(ranking_data, num_alternatives)
    validate_num_alternatives(num_alternatives)
    
    # Initialize candidate scores
    candidate_scores = {i: 0 for i in range(1, num_alternatives + 1)}

    # Convert ranking data into a list of ballots
    ballots = []
    for num_voters, ranks in ranking_data:
        ballots.extend([ranks] * num_voters)

    while True:
        # Reset candidate scores
        candidate_scores = {i: 0 for i in candidate_scores}

        # Count the first-choice votes for each candidate
        for ballot in ballots:
            if ballot:
                candidate_scores[ballot[0]] += 1

        # Check if any candidate has more than half of the votes
        total_votes = sum(candidate_scores.values())
        for candidate, votes in candidate_scores.items():
            if votes > total_votes / 2:
                return candidate  # Candidate wins

        # Find the candidate(s) with the fewest votes
        fewest_votes = min(candidate_scores.values())
        candidates_to_eliminate = [candidate for candidate, votes in candidate_scores.items() if votes == fewest_votes]

        # If all remaining candidates have the fewest votes, tiebreaker
        if len(candidates_to_eliminate) == len(candidate_scores):
            return candidates_to_eliminate  # Tiebreaker, return all, could be randomized for a candidate to win.

        # Eliminate the candidate(s) with the fewest votes
        for candidate in candidates_to_eliminate:
            del candidate_scores[candidate]

        # Remove the eliminated candidate(s) from each ballot and redistribute their votes
        for i in range(len(ballots)):
            ballots[i] = [candidate for candidate in ballots[i] if candidate not in candidates_to_eliminate]

# src/voting_rules/stv.py

from src.tools_for_distortion.utils.validators import validate_ranking_data

def single_transferable_vote(ranking_data, num_alternatives, num_winners):
    """
    Executes the Single Transferable Vote (STV) method for committee elections with fractional surplus redistribution.

    This method processes the voting data to elect a specified number of candidates. It uses an STV mechanism where each voter's ballot has a fractional value, initially set to 1. The method involves electing candidates who reach a vote quota and redistributing the surplus votes of elected candidates to the next preferences on the ballots. If no candidate reaches the quota, the candidate with the fewest votes is eliminated, and their votes are redistributed. This process continues until the required number of winners is elected.

    Args:
        ranking_data (list): A list of tuples, each containing the number of voters and their respective ranking of candidates.
        num_alternatives (int): The number of alternatives.
        num_winners (int): The number of candidates to be elected.

    Returns:
        list: A list of identifiers of the elected candidates.
    """
    # Validate inputs
    validate_ranking_data(ranking_data, num_alternatives)  # Validate ranking data

    total_votes = sum(num_voters for num_voters, _ in ranking_data)
    quota = total_votes // (num_winners + 1) + 1

    ballots = [{'ranking': ranks, 'value': 1.0} for num_voters, ranks in ranking_data for _ in range(num_voters)]
    elected_candidates = set()
    candidate_votes = {i: 0 for i in range(1, num_alternatives + 1)}

    while len(elected_candidates) < num_winners:
        for ballot in ballots:
            for candidate in ballot['ranking']:
                if candidate not in elected_candidates:
                    candidate_votes[candidate] += ballot['value']
                    break
        
        for candidate, votes in candidate_votes.items():
            if votes >= quota and candidate not in elected_candidates:
                elected_candidates.add(candidate)
                surplus = votes - quota
                surplus_ratio = surplus / votes
                for ballot in ballots:
                    if ballot['ranking'][0] == candidate:
                        ballot['value'] *= surplus_ratio
                        ballot['ranking'].pop(0)
                break
        else:
            min_votes = min(candidate_votes.values())
            for candidate, votes in candidate_votes.items():
                if votes == min_votes:
                    for ballot in ballots:
                        if candidate in ballot['ranking']:
                            ballot['ranking'].remove(candidate)
                    candidate_votes.pop(candidate)
                    break

    return list(elected_candidates)

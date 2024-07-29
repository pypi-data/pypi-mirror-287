
from collections import Counter
import src.tools_for_distortion.voting_rules as vr
from src.tools_for_distortion.data_parser import DataParser
import numpy as np

# Define custom ranking data for testing
ranking_data = [(3, [1, 2, 3]), (2, [2, 1, 3]), (1, [3, 2, 1])]


def test_plurality_scoring_rule():
    num_alternatives = 3
    result = vr.plurality_scoring_rule(ranking_data, num_alternatives)
    assert result == (1, 3), f"Expected (1, 3), got {result}"

def test_borda_scoring_rule():
    num_alternatives = 3
    result = vr.borda_scoring_rule(ranking_data, num_alternatives)
    assert result == (1, 8)

def test_harmonic_scoring_rule():
    num_alternatives = 3
    result = vr.harmonic_scoring_rule(ranking_data, num_alternatives)
    assert result[0] == 1, f"Expected (1, 4.333...), got {result}"
    assert round(result[1], 1) == 4.3

def test_instant_runoff_voting():
    num_alternatives = 3
    result = vr.instant_runoff_voting(ranking_data, num_alternatives)
    assert result == [1,2], f"Expected [1,2], got {result}"

def test_single_transferable_vote():
    ranking_data = [(3, [1, 2, 3]), (2, [2, 1, 3]), (1, [3, 2, 1])]
    num_alternatives = 3
    num_winners = 2
    result = vr.single_transferable_vote(ranking_data, num_alternatives, num_winners)
    assert result == [1, 2], f"Expected [1, 2], got {result}"

def test_probability_vector():
    ranking_data = [(3, [1, 2, 3]), (2, [2, 1, 3]), (1, [3, 2, 1])]
    num_alternatives = 3
    prob_vector = vr.harmonic_scoring_rule(ranking_data, num_alternatives, randomised=True)
    assert abs(sum(prob_vector.values()) - 1) < 1e-6, f"Probability vector does not sum up to 1: {sum(prob_vector.values())}"
    assert all(p >= 0 for p in prob_vector.values()), "Negative probabilities found"

def test_k_approval_multi_winner():
    num_alternatives = 3
    k = 2
    winners, scores = vr.k_approval_multi_winner(ranking_data, num_alternatives, k)
    assert len(winners) == k, f"Expected {k} winners, got {len(winners)}"
    highest_score = max(scores.values())
    assert all(score <= highest_score for score in scores.values()), "There is a score higher than the highest winner's score"

def test_boutilier_random_harmonic():
    num_alternatives = 3
    selection_counts = Counter()
    for _ in range(1000):
        selected_candidate = vr.boutilier_random_harmonic(ranking_data, num_alternatives)
        selection_counts[selected_candidate] += 1
    assert len(selection_counts) > 0, "No candidate selected"
    assert all(count > 0 for count in selection_counts.values()), "Some candidates never selected"

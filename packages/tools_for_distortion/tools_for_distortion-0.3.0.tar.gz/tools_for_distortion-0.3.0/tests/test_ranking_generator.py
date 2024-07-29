import random
import numpy as np

# Assuming the functions are imported here
from src.tools_for_distortion.ranking_generator import generate_rim_rankings, generate_single_peaked_preferences, format_rankings

# Set a seed for reproducibility in tests
random.seed(42)
np.random.seed(42)

def custom_distribution():
    return np.random.uniform(0, 1)

def test_format_rankings():
    rankings = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 3, 4]]
    parser = format_rankings(rankings)

    assert isinstance(parser.ranking_data, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in parser.ranking_data)
    assert parser.metadata['number_alternatives'] == 4

def test_generate_rim_rankings():
    num_voters = 10
    num_candidates = 4
    phi = 0.8

    parser = generate_rim_rankings(num_voters, num_candidates, phi)
    
    # Check ranking data structure
    assert isinstance(parser.ranking_data, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in parser.ranking_data)
    
    # Check metadata
    assert 'number_alternatives' in parser.metadata
    assert parser.metadata['number_alternatives'] == num_candidates

    # Check generated utilities
    parser.generate_utilities()
    assert all(len(utility) == num_candidates for utility in parser.utilities_data)
    assert all(0 <= u <= 1 for utility in parser.utilities_data for u in utility)

def test_generate_single_peaked_preferences():
    candidates = [1, 2, 3, 4, 5]
    num_voters = 10

    parser = generate_single_peaked_preferences(candidates, num_voters)

    # Check ranking data structure
    assert isinstance(parser.ranking_data, list), "ranking_data should be a list"
    assert all(isinstance(item, tuple) and len(item) == 2 for item in parser.ranking_data), "Each item in ranking_data should be a tuple of two elements"
    
    # Check metadata
    assert 'number_alternatives' in parser.metadata, "metadata should contain 'number_alternatives'"
    assert parser.metadata['number_alternatives'] == len(candidates), f"metadata['number_alternatives'] should be {len(candidates)}"
    
    # Check that each ranking in ranking_data is a list of integers
    for num_voters, ranking in parser.ranking_data:
        assert isinstance(ranking, list), "ranking should be a list"
        assert all(isinstance(candidate, int) for candidate in ranking), "ranking should be a list of integers"
        assert len(ranking) == len(candidates), f"ranking length should be {len(candidates)}"


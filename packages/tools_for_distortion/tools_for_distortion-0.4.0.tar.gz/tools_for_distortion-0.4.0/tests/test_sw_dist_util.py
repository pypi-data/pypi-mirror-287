from preflibtools.instances import OrdinalInstance
from collections import Counter
import src.tools_for_distortion.distortion as dist
from src.tools_for_distortion.data_parser import DataParser
import numpy as np


# Custom distribution function for utility generation
def custom_distribution():
    return np.random.uniform(0,1)

# so can use their external library or use our own parser.
instance = OrdinalInstance()
instance.parse_url("https://www.preflib.org/static/data/irish/00001-00000001.soi")

parser = DataParser()
metadata, ranking_data, utilities_data = parser.parse_data(instance, custom_distribution)

def test_utilities():
    
    num_candidates = int(metadata['number_alternatives'])

    for utility_vector in utilities_data:
        # Test 1: Sum of Utilities Equals One
        assert abs(sum(utility_vector) - 1) < 1e-6, "Test failed: Utilities do not sum up to 1"

        # Test 2: Length Equals Number of Candidates
        assert len(utility_vector) == num_candidates, "Test failed: Length of utilities vector does not match number of candidates"

        # Test 3: No Utility Value is Zero
        assert all(utility >= 0 for utility in utility_vector), "Test failed: Utility value is zero"

def test_det_distortion():
    winner = 2  # Example winner candidate id
    distortion = dist.det_distortion(winner, parser, num_iteres=10)
    assert distortion >= 0, "Distortion should be non-negative"
    
def test_multi_winner_distortion():
    winners = [1, 2, 3]  # Example list of winners
    _, worst_distortion = dist.multi_winner_distortion(winners, parser, num_iteres=10)
    assert worst_distortion >= 0, "Distortion should be non-negative"

def test_rand_distortion():
    probability_vector = [0.5, 0.25, 0.25]  # Example probabilities
    distortion = dist.rand_distortion(parser, probability_vector)
    assert distortion >= 0, "Distortion should be non-negative"
    
    
def test_social_welfare():
    utility_dic = dist.social_welfare(parser)
    assert all(value >= 0 for value in utility_dic.values()), "Social welfare values should be non-negative"

from src.tools_for_distortion.data_parser import DataParser
import numpy as np
from preflibtools.instances import OrdinalInstance

# Custom distribution function for utility generation
def custom_distribution():
    return np.random.uniform(0, 1)

# Initialize instance for testing
instance = OrdinalInstance()
instance.parse_url("https://www.preflib.org/static/data/irish/00001-00000001.soi")

def test_parsing_ranking_data():
    parser = DataParser()
    metadata, ranking_data, utilities_data = parser.parse_data(instance, custom_distribution)

    # Test the structure of ranking data
    assert isinstance(ranking_data, list), "Ranking data should be a list"
    assert all(isinstance(rank, tuple) and len(rank) == 2 for rank in ranking_data), "Each item in ranking data should be a tuple of two elements"

    # Test utilities are generated correctly
    assert all(len(utility) == metadata['number_alternatives'] for utility in utilities_data), "Each utility list should have the same length as number of alternatives"
    assert all(0 <= u <= 1 for utility in utilities_data for u in utility), "Utility values should be between 0 and 1"

    # Test metadata extraction
    assert 'number_alternatives' in metadata, "Number of alternatives should be in metadata"

    print("Parsing and data tests passed successfully.")

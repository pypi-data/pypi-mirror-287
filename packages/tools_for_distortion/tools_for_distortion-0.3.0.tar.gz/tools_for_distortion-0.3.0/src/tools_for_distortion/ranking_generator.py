import random
from src.tools_for_distortion.data_parser import DataParser
import src.tools_for_distortion.voting_rules as vr
import src.tools_for_distortion.distortion as dist

def format_rankings(rankings):
    """
    Formats the rankings into the required structure for further processing.
    
    Args:
    rankings (list of list of int): A list of rankings where each ranking is a list of candidate IDs.
    
    Returns:
    DataParser: An instance of DataParser containing the formatted rankings.
    """
    # Count the frequency of each ranking
    ranking_counts = {}
    for r in rankings:
        ranking_counts[tuple(r)] = ranking_counts.get(tuple(r), 0) + 1

    # Convert to the required format (num_voters, ranking)
    formatted_rankings = [(count, list(ranking)) for ranking, count in ranking_counts.items()]
    
    parser = DataParser()
    parser.ranking_data = formatted_rankings
    parser.ties_info = []
    for _, ranks in formatted_rankings:
        ties_group = [([candidate], 'single') for candidate in ranks]
        parser.ties_info.append(ties_group)
    parser.metadata = {'number_alternatives': len(rankings[0])}
    return parser

def generate_rim_rankings(num_voters, num_candidates, phi):
    """
    Generates rankings based on the Repeated Insertion Model (RIM).
    
    Args:
    num_voters (int): Total number of voters.
    num_candidates (int): Number of candidates (alternatives).
    phi (float): Dispersion parameter of the Mallows model.
    
    Returns:
    DataParser: An instance of DataParser containing the generated rankings.
    """
    def insertion_probability(i, j, phi):
        """
        Calculate the insertion probability for a candidate at a given position.
        
        Args:
        i (int): The step in the RIM process.
        j (int): The position at which the candidate is inserted.
        phi (float): Dispersion parameter of the Mallows model.
        
        Returns:
        float: The probability of insertion.
        """
        return phi**(i-j) / sum(phi**k for k in range(i))

    def generate_ranking(num_candidates, phi):
        """
        Generate a single ranking based on RIM.
        
        Args:
        num_candidates (int): Number of candidates.
        phi (float): Dispersion parameter of the Mallows model.
        
        Returns:
        list: The generated ranking.
        """
        ranking = []
        for i in range(1, num_candidates + 1):
            insert_pos = random.choices(range(1, i+1), 
                                        weights=[insertion_probability(i, j, phi) for j in range(1, i+1)])[0]
            ranking.insert(insert_pos - 1, i)
        return ranking

    # Generate the rankings
    rankings = [generate_ranking(num_candidates, phi) for _ in range(num_voters)]
    
    return format_rankings(rankings)

def generate_single_peaked_preferences(candidates, num_voters):
    """
    Generates single-peaked preferences for a list of candidates.
    
    Args:
    candidates (list of int): A list of candidate IDs.
    num_voters (int): Total number of voters.
    
    Returns:
    DataParser: An instance of DataParser containing the generated single-peaked preferences.
    """
    rankings = []
    # Randomly assign a peak preference for each voter
    for _ in range(num_voters):
        peak = random.choice(candidates)
        left_side = [c for c in candidates if c < peak]
        right_side = [c for c in candidates if c > peak]
        
        # Sort the left and right sides
        left_side.sort(reverse=True)
        right_side.sort()

        # Combine to form a single-peaked preference
        voter_pref = left_side + [peak] + right_side
        rankings.append(voter_pref)
    
    return format_rankings(rankings)

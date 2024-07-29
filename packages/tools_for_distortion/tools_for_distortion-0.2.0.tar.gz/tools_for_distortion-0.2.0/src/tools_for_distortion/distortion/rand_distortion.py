import random
from src.distortion.social_welfare import social_welfare

def rand_distortion(parser, probability_vector, method="expected", num_iters=100):
    """
    Calculates the distortion based on a random selection method.

    Args:
        parser (DataParser): An instance of the DataParser class.
        probability_vector (list): A list of probabilities for each candidate.
        method (str, optional): The method to calculate distortion ('expected' or 'average'). Defaults to "expected".
        num_iters (int, optional): Number of iterations for averaging in 'average' method. Defaults to 100.

    Returns:
        float: The calculated distortion value.
    """
    utility_dic = social_welfare(parser)
    
    if method == "expected":
        distortion_vector = [0 for _ in range(len(probability_vector))]
        for i, prob in enumerate(probability_vector):
            distortion_vector[i] = prob * utility_dic[i + 1]
        return max(utility_dic.values()) / sum(distortion_vector)
    
    elif method == "average":
        total_social_welfare = 0
        for _ in range(num_iters):
            winner = random.choices(range(1, len(probability_vector) + 1), weights=probability_vector, k=1)[0]
            total_social_welfare += utility_dic[winner]
        return max(utility_dic.values()) / (total_social_welfare / num_iters)

from src.distortion.det_distortion import det_distortion

def multi_winner_distortion(winners, parser, num_iteres=1, average=True):
    """
    Calculates the distortion for a list of winners in a multi-winner decision-making process.

    Args:
        winners (list): A list of winning candidate identifiers.
        parser (DataParser): An instance of the DataParser class.
        num_iteres (int, optional): Number of iterations for averaging. Defaults to 1.
        average (bool, optional): Flag to return average distortion over iterations. Defaults to True.

    Returns:
        tuple: A tuple containing the candidate with the worst distortion and the corresponding distortion value.
    """
    worst_cand, worst_distortion = None, 0
    for winner in winners:
        distortion = det_distortion(winner, parser, num_iteres, average)
        if distortion > worst_distortion:
            worst_cand, worst_distortion = winner, distortion
    return worst_cand, worst_distortion

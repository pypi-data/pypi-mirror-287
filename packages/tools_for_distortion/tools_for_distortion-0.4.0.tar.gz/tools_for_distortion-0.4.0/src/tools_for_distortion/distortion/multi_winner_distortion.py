from src.tools_for_distortion.distortion.det_distortion import social_welfare

def multi_winner_distortion(winners, parser, num_iteres=1, average=True):
    """
    Calculates the distortion for a list of winners in a multi-winner decision-making process.

    Args:
        winners (list): A list of winning candidate identifiers.
        parser (DataParser): An instance of the DataParser class.
        num_iteres (int, optional): Number of iterations for averaging. Defaults to 1.
        average (bool, optional): Flag to return average distortion over iterations. Defaults to True.

    Returns:
        float: The distortion value for the chosen committee.
    """
    distortions = []
    
    for _ in range(num_iteres):

        utility_dic = social_welfare(parser)
        chosen_committee_welfare = sum(utility_dic[winner] for winner in winners)
        optimal_committee_welfare = sum(sorted(utility_dic.values(), reverse=True)[:len(winners)])
        distortion = optimal_committee_welfare / chosen_committee_welfare
        distortions.append(distortion)

    if average:
        return sum(distortions) / len(distortions)
    else:
        return distortions[0]



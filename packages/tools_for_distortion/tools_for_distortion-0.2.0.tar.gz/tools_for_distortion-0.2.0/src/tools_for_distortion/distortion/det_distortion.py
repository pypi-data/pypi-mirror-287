from src.distortion.social_welfare import social_welfare

def det_distortion(winner, parser, num_iteres=1, average=True):
    """
    Calculates the distortion of a given winner in a deterministic voting rule for that setting. Could be average or worst case.
    
    Args:
        winner (int): The identifier of the winning candidate.
        parser (DataParser): An instance of the DataParser class, used to parse and handle the data.
        num_iteres (int, optional): The number of iterations to average over for distortion calculation. Defaults to 1.
        average (bool, optional): Flag to determine if the average distortion over iterations is returned or the worst case. Defaults to True.

    Returns:
        float: The calculated distortion value.
    """
    worst_distortion, total_distortion = 0, 0
    
    for iter in range(num_iteres):
        utility_dic = social_welfare(parser)
                
        # Finding the candidate with optimal social welfare
        optimal_sw = max(utility_dic.values())
        winner_sw = utility_dic[winner]

        # Calculating distortion
        if winner_sw > 0:
            distortion = optimal_sw / winner_sw
            total_distortion += distortion
            
            if distortion > worst_distortion:
                worst_distortion = distortion
        else:
            # Raise an error if winner's social welfare is zero
            raise ValueError(f"Winner's social welfare is zero in iteration {iter}. Please check the utility distribution or input data.")

    return total_distortion/num_iteres if average else worst_distortion

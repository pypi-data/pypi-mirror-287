from .social_welfare import social_welfare

def multi_winner_distortion(winners, parser, num_iteres=1, average=True):
    """
    Calculates the distortion for a given set of winners in a multi-winner setting.
    
    Args:
        winners (list): List of winning candidate ids.
        parser (DataParser): An instance of the DataParser class.
        num_iteres (int, optional): Number of iterations for averaging. Defaults to 1.
        average (bool, optional): Whether to return average distortion. Defaults to True.

    Returns:
        tuple: A tuple containing (average_distortion, worst_distortion).
    """
    worst_distortion, total_distortion = 0, 0

    for _ in range(num_iteres):
        utility_dic = social_welfare(parser)
        
        optimal_sw = sum(sorted(utility_dic.values(), reverse=True)[:len(winners)])
        winner_sw = sum(utility_dic[winner] for winner in winners)

        if winner_sw > 0:
            distortion = optimal_sw / winner_sw
            total_distortion += distortion
            
            if distortion > worst_distortion:
                worst_distortion = distortion
        else:
            raise ValueError("Winner's social welfare is zero. Check utility distribution or input data.")

    average_distortion = total_distortion / num_iteres if average else worst_distortion
    return average_distortion, worst_distortion

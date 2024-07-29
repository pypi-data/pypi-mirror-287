


def social_welfare(parser):
    """
    Calculates the social welfare for each candidate.

    Args:
        parser (DataParser): An instance of the DataParser class, used to parse and handle the data.

    Returns:
        dict: A dictionary with candidate identifiers as keys and their corresponding social welfare as values.
    """
    num_alternatives = int(parser.metadata['number_alternatives'])

    # this is wrong, because ties info is for only one voter's rankings at a time, not all voters.
    utilities_data = parser.generate_utilities()
    utility_dic = {i: 0 for i in range(1, num_alternatives + 1)}

    # Summing utilities for each candidate
    for voter_utility in utilities_data:
        for i, utility in enumerate(voter_utility):
            utility_dic[i + 1] += utility

    return utility_dic

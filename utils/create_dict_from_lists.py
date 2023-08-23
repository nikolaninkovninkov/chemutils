def create_dict_from_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")
    return_dict = {}
    for i in range(len(list1)):
        return_dict[list1[i]] = list2[i]
    return return_dict
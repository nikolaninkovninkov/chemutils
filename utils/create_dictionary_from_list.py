def create_dictionary_from_list(lst):
    dictionary = {}
    for i in range(0, len(lst), 2):
        key = lst[i]
        value = lst[i + 1]
        dictionary[key] = value
    return dictionary

def unique_values(lst):
    unique = []
    for value in lst:
        if value not in unique:
            unique.append(value)
    return unique
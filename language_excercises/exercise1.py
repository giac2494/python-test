def dict_values_ascending(dict_values):
    return sorted(dict_values.items(), key=lambda x: x[1])


dictionary = {
                'marco':'desk 1',
                'giulio':'desk 2',
                'mike':'room 3'
            }
print dict_values_ascending(dictionary)
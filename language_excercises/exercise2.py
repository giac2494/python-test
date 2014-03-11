def add_dict(dict_1, dict_2):
    return dict(dict_1.items() + dict_2.items())

dictionary1 = {
                'marco':'desk 1',
                'giulio':'desk 2',
                'mike':'room 3'
            }

dictionary2 = {
                'giacomo':'element 1',
                'leonardo':'ele 2',
                'john':'qualcosa'
            }
print add_dict(dictionary1, dictionary2)

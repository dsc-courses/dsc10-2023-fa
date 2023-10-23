test = {   'name': 'q2_4',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> result = calculate_similarity_for_all(favorite_uri, billions_club, ['Danceability', 'Energy', 'Valence', 'Acousticness'])\n"
                                               '>>> isinstance(result, np.ndarray) and isinstance(result[0], float)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> result = calculate_similarity_for_all(favorite_uri, billions_club, ['Danceability', 'Energy', 'Valence', 'Acousticness'])\n"
                                               '>>> len(result) == tswift.shape[0]\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

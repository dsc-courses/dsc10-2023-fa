test = {   'name': 'q2_3',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> features_1 = np.array([0.733, 0.71 , 0.965, 0.145])\n'
                                               '>>> features_2 = np.array([0.642 , 0.62  , 0.0969, 0.0734])\n'
                                               '>>> isinstance(calculate_similarity(features_1, features_2), float)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> features_1 = np.array([0.733, 0.71 , 0.965, 0.145])\n'
                                               '>>> features_2 = np.array([0.642 , 0.62  , 0.0969, 0.0734])\n'
                                               '>>> calculate_similarity(features_1, features_2) == calculate_similarity(features_2, features_1)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> features_1 = np.array([0.733, 0.71 , 0.965, 0.145])\n'
                                               '>>> features_2 = np.array([0.642 , 0.62  , 0.0969, 0.0734])\n'
                                               '>>> result = calculate_similarity(features_1, features_2)\n'
                                               '>>> np.isclose(result, 0.8804005736027208, rtol=1e-4)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> isinstance(favorite_vs_karma, float)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

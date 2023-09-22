test = {   'name': 'q2_8',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> callable(school_stats_multiple) and \\\n'
                                               "... isinstance(school_stats_multiple(['BERKELEY HIGH SCHOOL', 'CANYON CREST ACADEMY', 'TORREY PINES HIGH SCHOOL']), np.ndarray)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(school_stats_multiple(['CANYON CREST ACADEMY', 'TORREY PINES HIGH SCHOOL', 'BERKELEY HIGH SCHOOL']) == np.array([930, 179,  38]))\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(school_stats_multiple(['VINCENT MASSEY SECONDARY SCHOOL', 'CANYON CREST ACADEMY']) == np.array([0, 0, 0]))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

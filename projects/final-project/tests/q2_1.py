test = {   'name': 'q2_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(probabilities, bpd.Series) and len(probabilities) == 6\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(probabilities.sum(), 1)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(probabilities.loc['Asia'], 0.384311)\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.allclose([probabilities.loc[c] for c in ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Australia']], [0.3843107387661843, "
                                               '0.21165270373191164, 0.17547600913937547, 0.12113480578827114, 0.10072353389185072, 0.006702208682406703])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

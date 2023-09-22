test = {   'name': 'q4_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(observed_proportions, bpd.Series) and len(observed_proportions) == 6\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(observed_proportions.sum(), 1)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> total_since_1980 == 179\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(observed_proportions.loc['Asia'], 0.384615, rtol=0.01)\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.allclose([observed_proportions.loc[c] for c in ['Africa', 'Asia', 'Australia', 'Europe', 'North America', 'South America']], "
                                               '[0.24022346368715083, 0.3854748603351955, 0.01675977653631285, 0.12290502793296089, 0.18435754189944134, 0.05027932960893855])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

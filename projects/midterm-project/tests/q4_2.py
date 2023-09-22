test = {   'name': 'q4_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> # This checks that you've spelled all counties correctly!\n"
                                               ">>> all_counties = ['Sonoma', 'Napa', 'Solano', 'Marin', 'Contra Costa', 'Alameda', 'San Mateo', 'San Francisco', 'Santa Clara', 'Kern', 'San "
                                               "Bernardino', 'Los Angeles', 'Santa Barbara', 'San Diego', 'Imperial', 'Riverside', 'Orange', 'San Luis Obispo', 'Ventura']\n"
                                               '>>> outputs = np.array([bay_or_socal(c) for c in all_counties])\n'
                                               ">>> np.all((outputs == 'bay_area') | (outputs == 'socal'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> [bay_or_socal('Solano'), bay_or_socal('San Diego'), bay_or_socal('Santa Cruz')] == ['bay_area', 'socal', 'neither']\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

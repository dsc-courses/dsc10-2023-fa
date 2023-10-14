test = {   'name': 'q4_5',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> '(No previous year)' not in with_previous_fortune_500.get('% Change')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> with_previous_fortune_500.shape[0] == 471\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> t = with_previous_fortune_500.sort_values(by='Previous_Revenue', ascending=False)\n"
                                               ">>> value = t.get('Previous_Revenue').values[0]\n"
                                               '>>> np.isclose(value, 571299065420.5607)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

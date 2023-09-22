test = {   'name': 'q4_6',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> "(No previous year)" not in with_previous_compensation.get("% Change")\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> t = with_previous_compensation.sort_values(by="Previous_Total_Pay", ascending=False)\n'
                                               '>>> value = t.get("Previous_Total_Pay").values[0]\n'
                                               '>>> np.isclose(value, 67700000.0)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> with_previous_compensation.shape[0] == 81\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

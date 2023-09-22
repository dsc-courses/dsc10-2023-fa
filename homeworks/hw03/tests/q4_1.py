test = {   'name': 'q4_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> type(colleges) == dict and len(colleges) == 7\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # This test makes sure that all of your values are emojis recognized by our autograder.\n'
                                               ">>> all_emojis = read_json('data/emojis.json')\n"
                                               '>>> \n'
                                               '>>> invalid_keys = []\n'
                                               '>>> for k in colleges.keys():\n'
                                               '...     if colleges[k] not in all_emojis:\n'
                                               '...         invalid_keys.append(k)\n'
                                               '>>> \n'
                                               '>>> if len(invalid_keys) == 0:\n'
                                               "...     print('All valid')\n"
                                               '... else:\n'
                                               "...     print('The emoji(s) corresponding to the key(s) ' + str(invalid_keys)[1:-1] + ' are invalid.\\nCheck your work!')\n"
                                               'All valid\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This test makes sure that all values in colleges are of length 1.\n>>> all([len(e) == 1 for e in colleges.values()])\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> sorted(list(colleges.keys())) == ['<ERC>', '<Marshall>', '<Muir>', '<Revelle>', '<Seventh>', '<Sixth>', '<Warren>']\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

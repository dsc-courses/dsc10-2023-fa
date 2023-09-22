test = {   'name': 'q2_6',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> (result == 'These were some yummy nachos!') or (result ==  'These nachos were disappointing.') or (result == 'These nachos were hit or miss.')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> ten_nachos = np.array(['neither', 'cheese', 'both', 'both', 'cheese', 'salsa', 'both', 'neither', 'cheese', 'both'])\n"
                                               '>>> ten_nachos_reactions = bpd.DataFrame().assign(Nacho=ten_nachos)\n'
                                               '>>> ten_nachos_reactions = ten_nachos_reactions.assign(Reaction=ten_nachos_reactions.get("Nacho").apply(nacho_reaction))\n'
                                               ">>> both_or_neither(ten_nachos_reactions) == 'These were some yummy nachos!'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> seven_nachos = np.array(['neither', 'cheese', 'both', 'both', 'neither', 'both', 'neither'])\n"
                                               '>>> seven_nachos_reactions = bpd.DataFrame().assign(Nacho=seven_nachos)\n'
                                               '>>> seven_nachos_reactions = seven_nachos_reactions.assign(Reaction=seven_nachos_reactions.get("Nacho").apply(nacho_reaction))\n'
                                               ">>> both_or_neither(seven_nachos_reactions) == 'These nachos were hit or miss.'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

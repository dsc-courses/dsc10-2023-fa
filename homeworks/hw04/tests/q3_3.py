test = {   'name': 'q3_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(boot_dark_proportions, np.ndarray) and len(boot_dark_proportions) == 1000\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.all(np.isclose(boot_dark_proportions, dark_proportion)) == False # It looks like all of your resamples have the same mean – take a closer look '
                                               "at how you're resampling!\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

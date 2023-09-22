test = {   'name': 'q3_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(resample_means, np.ndarray) and len(resample_means) == 1000\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.all(np.isclose(resample_means, cathy_mean)) == False # It looks like all of your resamples have the same mean – take a closer look at how '
                                               "you're resampling!\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

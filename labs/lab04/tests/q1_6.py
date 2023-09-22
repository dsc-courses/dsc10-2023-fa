test = {   'name': 'q1_6',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> ok_test_array = np.array([1, 2, 3, 4, 5, 6, 7])\n>>> abs(11 - (np.mean(ok_test_array) - calculate_mean_based_estimate(ok_test_array))) < 4\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> ok_test_array = np.array([5, 4, 3, 6, 7, 1, 4, 12, 8])\n'
                                               '>>> abs(11 - (np.mean(ok_test_array) - calculate_mean_based_estimate(ok_test_array))) < 4\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> abs(11 - (np.mean(observations) - calculate_mean_based_estimate(observations))) < 4\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

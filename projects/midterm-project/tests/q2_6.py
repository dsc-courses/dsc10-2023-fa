test = {   'name': 'q2_6',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> output_df = song_recommender('7w87IxuO7BDcJ3YUqCyMTT', billions_club, 5)\n"
                                               '>>> isinstance(output_df, bpd.DataFrame) and output_df.shape == (5, 9)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> output_df = song_recommender('7w87IxuO7BDcJ3YUqCyMTT', billions_club, 10, feature_list=['Energy', 'Speechiness'])\n"
                                               '>>> isinstance(output_df, bpd.DataFrame) and output_df.shape == (10, 4)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

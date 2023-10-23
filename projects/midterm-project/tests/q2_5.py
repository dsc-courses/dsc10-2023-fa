test = {   'name': 'q2_5',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> similarity_scores = calculate_similarity_for_all('7w87IxuO7BDcJ3YUqCyMTT', billions_club, ['Danceability', 'Energy', 'Valence', 'Acousticness'])\n"
                                               '>>> output_df = select_top_recommendations(similarity_scores, 5)\n'
                                               '>>> isinstance(output_df, bpd.DataFrame) and output_df.shape == (5, 20)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

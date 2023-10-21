test = {   'name': 'q2_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> ten_coffees_df.shape == (10, 2)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> coffee_price(ten_coffees_df.get('Size').loc[4]) in [2.99, 3.99, 4.79, 4.99]\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> coffee_price(ten_coffees_df.get('Size').loc[4]) == ten_coffees_df.get('Price').loc[4]\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

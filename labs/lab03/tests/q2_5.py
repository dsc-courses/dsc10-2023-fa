test = {   'name': 'q2_5',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> (result == 'More Large coffees') or (result ==  'More Extra Large coffees') or (result == 'Same amount') # Check spelling and capitalization!\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> ten_coffees = np.array(['Large', 'Extra Large', 'Small', 'Large', 'Medium', 'Small', 'Extra Large', 'Small', 'Small', 'Large'])\n"
                                               '>>> ten_coffees_prices = bpd.DataFrame().assign(Size=ten_coffees)\n'
                                               '>>> ten_coffees_prices = ten_coffees_prices.assign(Price=ten_coffees_prices.get("Size").apply(coffee_price))\n'
                                               ">>> large_or_xl(ten_coffees_prices) == 'More Large coffees'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> seven_coffees = np.array(['Medium', 'Extra Large', 'Large', 'Medium', 'Small', 'Extra Large', 'Large'])\n"
                                               '>>> seven_coffees_prices = bpd.DataFrame().assign(Size=seven_coffees)\n'
                                               '>>> seven_coffees_prices = seven_coffees_prices.assign(Price=seven_coffees_prices.get("Size").apply(coffee_price))\n'
                                               ">>> large_or_xl(seven_coffees_prices) == 'Same amount'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

OK_FORMAT = True

test = {   'name': 'q3_1',
    'points': [1, 5],
    'suites': [   {   'cases': [   {'code': '>>> len(resample_yes_proportions) == 10000\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> abs(np.mean(resample_yes_proportions) - 0.525) < 0.025 and np.std(resample_yes_proportions) < 0.08\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

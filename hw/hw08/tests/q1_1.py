OK_FORMAT = True

test = {   'name': 'q1_1',
    'points': [0, 0, 2],
    'suites': [   {   'cases': [   {'code': '>>> type(one_resampled_percentage(votes)) in set([float, np.float64])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> one_resampled_percentage(votes) <= 0\nFalse', 'hidden': False, 'locked': False},
                                   {'code': '>>> 35 <= one_resampled_percentage(votes) <= 65\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

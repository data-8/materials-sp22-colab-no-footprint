OK_FORMAT = True

test = {   'name': 'q1_3',
    'points': [0, 0, 2],
    'suites': [   {   'cases': [   {'code': ">>> type(fit_line(Table().with_columns('x', make_array(0, 1), 'y', make_array(1, 3)), 'x', 'y')) == np.ndarray\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> len(fit_line(Table().with_columns('x', make_array(0, 1), 'y', make_array(1, 3)), 'x', 'y')) == 2\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.allclose(np.round(fit_line(Table().with_columns('x', make_array(0, 1), 'y', make_array(1, 3)), 'x', 'y'), 5), np.array([2, 1]))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

OK_FORMAT = True

test = {   'name': 'q2_1_4',
    'points': [0, 0, 0],
    'suites': [   {   'cases': [   {'code': ">>> set(close_movies.labels) >= {'Genre', 'Title', 'feel', 'water'}\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> close_movies.num_rows == 5\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> close_movies.column('Title').item(0) != 'monty python and the holy grail'\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

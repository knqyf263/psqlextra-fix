# psqlextra_fix

## Prepare
Of course, you can use pip instead of pipenv.

```
$ pipenv install
$ pipenv shell
$ python manage.py migrate
$ docker run -d --name postgres -p 5432:5432 postgres:10.3-alpine
```

## Test

```
$ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
<PostgresQuerySet [{'name': 'group2', 'age': None}, {'name': 'group1', 'age': 30}]>
.E
======================================================================
ERROR: test_union_exception (users.tests.GroupTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/teppei/src/github.com/knqyf263/psqlextra_fix/users/tests.py", line 23, in test_union_exception
    print(group)
  File "/Users/teppei/src/github.com/knqyf263/psqlextra_fix/.venv/lib/python3.6/site-packages/django/db/models/query.py", line 248, in __repr__
    data = list(self[:REPR_OUTPUT_SIZE + 1])
  File "/Users/teppei/src/github.com/knqyf263/psqlextra_fix/.venv/lib/python3.6/site-packages/django/db/models/query.py", line 272, in __iter__
    self._fetch_all()
  File "/Users/teppei/src/github.com/knqyf263/psqlextra_fix/.venv/lib/python3.6/site-packages/django/db/models/query.py", line 1179, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "/Users/teppei/src/github.com/knqyf263/psqlextra_fix/.venv/lib/python3.6/site-packages/django/db/models/query.py", line 106, in __iter__
    for row in compiler.results_iter(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size):
  File "/Users/teppei/src/github.com/knqyf263/psqlextra_fix/.venv/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 1011, in apply_converters
    value = converter(value, expression, connection)
  File "/Users/teppei/src/github.com/knqyf263/psqlextra_fix/.venv/lib/python3.6/site-packages/django/db/models/expressions.py", line 317, in <lambda>
    return lambda value, expression, connection: None if value is None else int(value)
ValueError: invalid literal for int() with base 10: 'test'

----------------------------------------------------------------------
Ran 2 tests in 0.048s
```



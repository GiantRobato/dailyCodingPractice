
Libraries used:

- flask - simple web server application
- flask_caching - extension to flask that adds caching support
- pandas - a hack to select data from table of values instead of creating an actual db

To test for speed we can use curl's in built timing feature with the -w flag

```bash
$ curl localhost:5000/get_voters_where?county=Adams&month=1&party=Democrat&limit=3&status=Active -w "@curl-format.txt" -o /dev/null
```

without cache: ~4 seconds for a query

with cache:

- first time: ~3.864 seconds
- following: ~0.032 seconds

a ~100x speedup

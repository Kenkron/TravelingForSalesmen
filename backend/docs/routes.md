Routes
======

GET /ping
---------

Returns a status code of 200 to show the server is up.
Does not return data.

POST /min_span
--------------

Runs a minimum spanning tree for a list of points, and returns
the edges.

The input must be a JSON object with the key
`points`, which must be a list of points, each of which is a
two element list.  The output is a JSON object with a single
key `edges`, which stores a list of pairs of points as indexes
to the original input.

sample input data:

```
{
    "points": [
        [0, 0],
        [1, 1]
    ]
}
```

sample output data:

```
{
    "edges": [
        [0, 1]
    ]
}
```

POST /traveling_salesman
------------------------

Finds an approximate solution to the traveling
salesman problem for a list of points.

The input must be a JSON object with the key
`points`, which must be a list of points, each of which is a
two element list.  The output is a JSON object with a single
key `path`, which stores an ordered list of points the same
way as the `points` key in the input.

sample input data:

```
{
    "points": [
        [0.1, 0],
        [1, 1],
        [0, 1]
    ]
}
```

sample output data:

```
{
    "path": [
        [0.1, 0.0],
        [0.0, 1.0],
        [1.0, 1.0]
    ]
}
```

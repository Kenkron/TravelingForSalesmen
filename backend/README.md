Traveling for Salesemen Backend
===============================

This is a flask application that approximates a solution to the traveling
salesmen problem.

It walks a minimum spanning tree to get a path that is no worse than twice as
long as optimial. The path is then cleaned by uncrossing overlapping line
segments.

Compilation
-----------

For performance, the application has a backend written in c for the minimum
spanning tree. This code is stored in the *native* folder, and on linux, can
be compiled with the following code.

```
cd native
make
```

Testing
-------

The file *test_main.py* can perform 100% coverage of *main.py*, and is
required to do so by github actions for pull requests with master.

```
python test_main.py
```

Alternatively, for coverage

```
coverage run test_main.py
coverage report --fail-under=100 -m main.py
```

Deployment
----------

For deployment, the application has a *Dockerfile* and a *docker-compose* file
in the *docker* folder. The docker image should be created from the *backend*
folder as follows.

```
docker build -f docker/Dockerfile --tag traveling-for-salesmen .
```

When run, the image must publish port 8080

```
docker run -p 8000:8080 traveling-for-salesmen
```

Alternatively, it can be run with docker-compose

```
cd docker
docker-compose up -d
```

Styling
-------

This code is required to pass flake8 linting for pull requests with master.

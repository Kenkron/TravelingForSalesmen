Traveling for Salesmen
======================

The traveling salesman problem is famously unsolvable. However, salesmen find
their way around anyways, and this application illustrates that.

It uses a backend written in flask, which in tern uses a python native
interface, to find a minimium spanning tree for a list of inputs.
Walking along this provides a satisfactory, if imperfect, approximation
of the traveling salesman probem guareanteed to be no worse than
twice the length of the optimal solution.

For mor information on the backend, see the README in the backend folder.


The frontend is written using vue.js, and is simply an interface for
interacting with the backend API. It shows a map, and allows the user
to click on locations they would like to visit, before querying
the api for the shortest (or at least, a somewhat short) path connecting
all points.

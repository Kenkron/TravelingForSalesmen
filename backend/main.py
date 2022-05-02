import json
from numbers import Real

from flask import Flask
from flask import request
from flask import abort

import min_span as min_span_lib

app = Flask(__name__)

def validate_point_list(data):
    """
    Validates a point list, and returns
    it as a list of tuples.
    """
    if type(data) is not list:
        return abort(422, "data is not a list")
    tuple_points = []
    for p in data:
        if type(p) is not list:
            return abort(422, "found non-list point")
        if len(p) != 2:
            return abort(422, "found non-2d point")
        if not (isinstance(p[0], Real) and isinstance(p[1], Real)):
            return abort(422, "found non-numeric point")
        tuple_points.append(tuple(p))
    return tuple_points

@app.route("/ping")
def route_ping():
    print("ping")
    return ""

@app.route("/min_span")
def route_min_span():
    """
    Runs a minimum spanning tree for a list of points
    """
    json_data = request.get_json()
    if "points" not in json_data:
        return abort(422, "points not found")
    data = json_data["points"]
    points = validate_point_list(data)
    return {"edges": min_span_lib.min_span_c(points)}

@app.route("/traveling_salesman")
def route_traveling_salesman():
    """
    Finds an approximate solution to the traveling
    salesman problem for a list of points
    """
    json_data = request.get_json(force=True)
    if "points" not in json_data:
        return abort(422, "points not found")
    data = json_data["points"]
    points = validate_point_list(data)
    return json.dumps(
        {"path": min_span_lib.traveling_salesman_from_edges(points)})

if __name__ == "__main__": # pragma: no cover
    app.run()

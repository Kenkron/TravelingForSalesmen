import json
import unittest
from main import app

class AppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    def test_ping(self):
        response = self.app.get('/ping', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_min_span(self):
        msg = "should respond with a single edge between (0,0) and (1,1)"
        points = [
            [0, 0],
            [1, 1]]
        # Order is not important here
        expected_as_set = {0, 1}
        response = self.app.get(
            "/min_span",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        output = json.loads(response.data)
        self.assertTrue("edges" in output)
        self.assertEqual(len(output["edges"]), 1)
        edge = output["edges"][0]
        self.assertEqual(set(edge), expected_as_set, msg)

        msg = "empty input should produce empty output"
        points = []
        expected = []
        response = self.app.get(
            "/min_span",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        output = json.loads(response.data)
        self.assertEqual(output["edges"], expected, msg)

        msg = "input with a single point should produce empty output"
        points = [[0, 0]]
        expected = []
        response = self.app.get(
            "/min_span",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        output = json.loads(response.data)
        self.assertEqual(output["edges"], expected, msg)

        msg = "input with duplicate points should be valid"
        points = [
            [0, 0],
            [0, 0]]
        # Order is not important here
        expected_as_set = {0, 1}
        response = self.app.get(
            "/min_span",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        output = json.loads(response.data)
        self.assertTrue("edges" in output)
        self.assertEqual(len(output["edges"]), 1)
        edge = output["edges"][0]
        self.assertEqual(set(edge), expected_as_set, msg)

        msg = "input without data should throw a 400"
        response = self.app.get(
            "/min_span",
            follow_redirects=True,
            content_type="application/json")
        self.assertEqual(response.status_code, 400, msg)
        
        msg = "input without points should throw a 422"
        response = self.app.get(
            "/min_span",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({}))
        self.assertEqual(response.status_code, 422, msg)

        msg = "input with points as a non-list should throw a 422"
        points = { "x": [0, 1], "y": [0, 1] }
        response = self.app.get(
            "/min_span",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        self.assertEqual(response.status_code, 422, msg)

        msg = "input with non-list points should throw a 422"
        points = [
            {"x": 0, "y": 0},
            {"x": 1, "y": 1}]
        response = self.app.get(
            "/min_span",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        self.assertEqual(response.status_code, 422, msg)

        msg = "input with non-numeric points should throw a 422"
        points = [
            ["0", "0"],
            ["1", "1"]]
        response = self.app.get(
            "/min_span",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        self.assertEqual(response.status_code, 422, msg)

    def test_traveling_salesman(self):

        msg = "should respond with a single path between (0,0) and (1,1)"
        points = [
            [0, 0],
            [1, 1]]
        # Order is not important here
        expected_as_set = {(0, 0), (1, 1)}
        response = self.app.get(
            "/traveling_salesman",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        output = json.loads(response.data)
        output_set = set()
        for o in output["path"]:
            output_set.add((o[0], o[1]))
        self.assertEqual(set(output_set), expected_as_set, msg)

        msg = "input with no points should respond with an empty path"
        points = []
        expected = []
        response = self.app.get(
            "/traveling_salesman",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        output = json.loads(response.data)
        self.assertEqual(output["path"], expected, msg)

        msg = "input with only one point should respond with that point"
        points = [[1, 2]]
        expected = [[1, 2]]
        response = self.app.get(
            "/traveling_salesman",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        output = json.loads(response.data)
        self.assertEqual(output["path"], expected, msg)

        msg = "input without data should throw a 400"
        response = self.app.get(
            "/traveling_salesman",
            follow_redirects=True,
            content_type="application/json")
        self.assertEqual(response.status_code, 400, msg)
        
        msg = "input without points should throw a 422"
        response = self.app.get(
            "/traveling_salesman",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({}))
        self.assertEqual(response.status_code, 422, msg)

        msg = "input with points as a non-list should throw a 422"
        points = { "x": [0, 1], "y": [0, 1] }
        response = self.app.get(
            "/traveling_salesman",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        self.assertEqual(response.status_code, 422, msg)

        msg = "input with non-list points should throw a 422"
        points = [
            {"x": 0, "y": 0},
            {"x": 1, "y": 1}]
        response = self.app.get(
            "/traveling_salesman",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        self.assertEqual(response.status_code, 422, msg)

        msg = "input with non-numeric points should throw a 422"
        points = [
            ["0", "0"],
            ["1", "1"]]
        response = self.app.get(
            "/traveling_salesman",
            follow_redirects=True,
            content_type="application/json",
            data=json.dumps({"points": points}))
        self.assertEqual(response.status_code, 422, msg)

if __name__ == "__main__":
    unittest.main()

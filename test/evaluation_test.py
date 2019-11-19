#!usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from src.database import Database
from src.utils import read_json


class EvaluationTest(unittest.TestCase):
    """
    This class contains test methods to test the extraction of status from handmade graph and from json.
    """
    def test_evaluation_1(self):
        # Reference test
        reference_status = {"img001": "granularity_staged", "img002": "valid"}

        # Initial graph
        build = [
            ("core", None),
            ("A", "core"),
            ("B", "core"),
            ("C", "core"),
            ("C1", "C"),
        ]
        # Extract
        extract = {"img001": ["A"], "img002": ["C1"]}
        # Graph edits
        edits = [("A1", "A"), ("A2", "A")]

        # Get status (this is only an example, test your code as you please as long as it works)
        status = {}
        if len(build) > 0:
            # Build graph
            db = Database(build[0][0])
            if len(build) > 1:
                db.add_nodes(build[1:])
            # Add extract
            db.add_extract(extract)
            # Graph edits
            db.add_nodes(edits)
            # Update status
            status = db.get_extract_status()

        # Test if the status are the same, if yes, process is done correctly
        self.assertEqual(status, reference_status)

    def test_evaluation_2(self):
        # Reference test
        reference_status = {
            "img001": "granularity_staged",
            "img002": "coverage_staged",
            "img003": "invalid",
        }

        # Initial graph
        build = [
            ("core", None),
            ("A", "core"),
            ("B", "core"),
            ("C", "core"),
            ("C1", "C"),
        ]
        # Extract
        extract = {"img001": ["A", "B"], "img002": ["A", "C1"], "img003": ["B", "E"]}
        # Graph edits
        edits = [("A1", "A"), ("A2", "A"), ("C2", "C")]

        # Get status (this is only an example, test your code as you please as long as it works)
        status = {}
        if len(build) > 0:
            # Build graph
            db = Database(build[0][0])
            if len(build) > 1:
                db.add_nodes(build[1:])
            # Add extract
            db.add_extract(extract)
            # Graph edits
            db.add_nodes(edits)
            # Update status
            status = db.get_extract_status()

        # Test if the status are the same, if yes, process is done correctly
        self.assertEqual(status, reference_status)

    def test_evaluation_json(self):
        # Reference test
        reference_status = read_json("../data/expected_status.json")

        # Initial graph
        build = read_json("../data/graph_build.json")
        # Extract
        extract = read_json("../data/img_extract.json")
        # Graph edits
        edits = read_json("../data/graph_edits.json")

        # Get status (this is only an example, test your code as you please as long as it works)
        status = {}
        if len(build) > 0:
            # Build graph
            db = Database(build[0][0])
            if len(build) > 1:
                db.add_nodes(build[1:])
            # Add extract
            db.add_extract(extract)
            # Graph edits
            db.add_nodes(edits)
            # Update status
            status = db.get_extract_status()

        # Test if the status are the same, if yes, process is done correctly
        self.assertEqual(status, reference_status)


if __name__ == "__main__":
    unittest.main()

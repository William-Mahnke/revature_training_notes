# ═══════════════════════════════════════════════════════
# Loading Test Data
# ═══════════════════════════════════════════════════════
# As test suites grow, hard-coding test values directly into
# test methods becomes unwieldy when the same logic needs to
# be tested against many inputs.
#
# Externalising test data into files (e.g. CSV, JSON) keeps
# test methods clean and focused on behaviour.
#
# Key concepts demonstrated here:
#   - Loading test data from a CSV file using csv.DictReader
#   - Building reliable file paths using os.path and __file__
#   - Using subTest() to run the same assertion against multiple
#     inputs, reporting each failure individually
#
# subTest(msg) — a context manager that wraps each iteration of
# a loop. Unlike a plain loop, subTest does not stop at the first
# failure — all inputs are tested and all failures are reported.
# ═══════════════════════════════════════════════════════
import unittest
import csv
import os

# Dummy method that we are testing using our input data (csv)
# is_passing() represents a simple business rule: a score of
# 50 or above is considered a passing grade.
def is_passing(score):
    return score >= 50

class TestLoadingData(unittest.TestCase):

    def setUp(self):
        # setUp() runs before each test method, providing a clean state.
        # Here it builds the path to the data directory relative to this
        # test file using os.path.dirname(__file__).
        #
        # Using __file__ (the path of this script) rather than a hardcoded
        # absolute path ensures the tests work regardless of where in the
        # file system the project is located or from which directory the
        # tests are run.
        self.data_dir = os.path.join(os.path.dirname(__file__), "data")

    # test method using our dummy data
    def test_passing_scores_from_csv(self):
        csv_path = os.path.join(self.data_dir, "test_data.csv")

        # Load test data using csv_path - reading data into 'rows'
        # csv.DictReader reads the CSV and maps each row to a dictionary
        # using the header row as keys. Each row is then accessible as
        # row['name'], row['score'], etc.
        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Check the 'is_passing' method against each row from our reader
        for row in rows:
            # the score of each row — cast to int since CSV values are strings
            score = int(row['score'])

            # subTest reports each failure individually, rather than stopping at the first.
            # The name= and score= arguments are labels that appear in the failure output,
            # making it easy to identify exactly which row caused the failure.
            with self.subTest(name=row['name'], score=score):
                # The result from our method call
                result = is_passing(score)

                # What we expect the function to do
                expected = score >= 50

                # Checking the actual vs expected
                self.assertEqual(result, expected)

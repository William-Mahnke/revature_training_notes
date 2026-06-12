# ═══════════════════════════════════════════════════════
# Loading Test Data — Extended Example
# ═══════════════════════════════════════════════════════
# This file extends the CSV data loading pattern from
# test_004_loading_data.py to a more complex scenario:
# testing a multi-branch grading function against a richer
# dataset that includes an expected output column ('grade').
#
# Rather than computing the expected result inside the test
# (as in test_004), the expected value is read directly from
# the CSV alongside the input. This pattern is useful when
# the expected output is complex or pre-computed externally.
#
# The CSV (test_data_graded.csv) has three columns:
#   name  — the student's name (label only, not used in logic)
#   score — the numeric score (input to the function under test)
#   grade — the expected letter grade (expected output)
# ═══════════════════════════════════════════════════════
import unittest
import csv
import os

# The function under test — returns a letter grade based on the numeric score.
# This multi-branch function is a good candidate for data-driven testing
# because each branch (A/B/C/D/F) needs to be exercised with representative
# input values, which can be conveniently stored in the CSV.
def grader(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

class TestLoadingData(unittest.TestCase):

    def setUp(self):
        # Builds the path to the data directory relative to this test file.
        # See test_004_loading_data.py for a full explanation of this pattern.
        self.data_dir = os.path.join(os.path.dirname(__file__), "data")

    def test_passing_scores_from_csv(self):
        # test_data_graded.csv contains three columns: name, score, grade.
        # The 'grade' column holds the pre-computed expected output for each row,
        # allowing the test to compare the function's result directly against it.
        csv_path = os.path.join(self.data_dir, "test_data_graded.csv")

        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        for row in rows:
            score = int(row['score'])
            # Read the expected grade from the CSV — cast to str for safety
            grade = str(row['grade'])

            # subTest wraps each row so all failures are reported independently.
            # The name=, score=, and grade= labels appear in failure output,
            # making it immediately clear which row failed and what was expected.
            with self.subTest(name=row['name'], score=score, grade=grade):
                result = grader(score)

                # Checking the actual vs expected
                self.assertEqual(result, grade)

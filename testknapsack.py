import unittest
from KnapSack import knapsack

class TestKnapsack(unittest.TestCase):
    def test_knapsack(self):
        # Test case 1: Provide a sample test case
        values = [60, 100, 120]
        weights = [10, 20, 30]
        limit = 50
        expected_solution = ([0, 1, 1], 220)  # Expected solution and objective
        solution, objective = knapsack(len(values), values, weights, limit)
        self.assertEqual(solution, expected_solution[0])
        self.assertEqual(objective, expected_solution[1])
        #Testing that the function returns the expected solution and the objective
        # Add more test cases for different scenarios

if __name__ == '__main__':
    unittest.main()

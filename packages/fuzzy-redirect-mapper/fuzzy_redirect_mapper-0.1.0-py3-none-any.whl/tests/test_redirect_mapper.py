import unittest
from fuzzy_redirect_mapper import compare_urls_in_csv

class TestRedirectMapper(unittest.TestCase):
    def test_compare_urls_in_csv(self):
        file_name = "test_urls.csv"
        column1 = "source"
        column2 = "destination"
        result_df = compare_urls_in_csv(file_name, column1, column2)
        self.assertTrue(len(result_df) > 0)

if __name__ == '__main__':
    unittest.main()

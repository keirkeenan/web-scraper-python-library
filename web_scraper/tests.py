# disable the following pylint warnings:
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=wrong-import-position

import sys
import unittest

sys.path.append('../')
from web_scraper.main import get_html, parse_itemprice, scrape_ebay, scrape_walmart, scrape_amazon, scrape


class TestMethods(unittest.TestCase):
    # Test the get_html function

    def test_ebay(self):
        # Test with valid input
        html = get_html("ebay", "iphone 12", 1)
        self.assertTrue("<!DOCTYPE html>" in html)

    # def test_walmart(self):
    #     # Test with valid input
    #     html = get_html("walmart", "iphone 12", 1)
    #     self.assertTrue("<!DOCTYPE html>" in html)

    def test_amazon(self):
        # Test with valid input
        html = get_html("amazon", "iphone 12", 1)
        self.assertTrue("<!doctype html>" in html)

    def test_wrong_company_name(self):
        # Test with invalid input
        html = get_html("wrong", "iphone 12", 1)
        self.assertEqual(html, "Something went wrong. Please try again.")

    # ===================================#

    # Test the parse_itemprice function

    def test_parse_itemprice_valid(self):
        # Test with valid input
        text = "$123.45"
        expected_output = 123.45
        self.assertEqual(parse_itemprice(text), expected_output)

    # ===================================#

    # Test the scrape functions

    def test_scrape_ebay_valid(self):
        # Test with valid input
        result = scrape_ebay("iphone 12")
        not_expected_output = "Failed to collect data from eBay. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"

        self.assertNotEqual(result, not_expected_output)

    def test_scrape_walmart_valid(self):
        # Test with valid input
        result = scrape_walmart("iphone 12")
        not_expected_output = "Failed to collect data from Walmart. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
        self.assertNotEqual(result, not_expected_output)

    def test_scrape_amazon_valid(self):
        # Test with valid input
        result = scrape_amazon("iphone 12")
        not_expected_output = "Failed to collect data from Amazon. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
        self.assertNotEqual(result, not_expected_output)

    # ===================================#

    # Test the main function

    def test_main_valid(self):
        # Test with valid input
        result = scrape("iphone 12", "ebay")
        not_expected_output = "Failed to collect data from eBay."
        self.assertNotEqual(result, not_expected_output)

    def test_main_invalid(self):
        # Test with invalid input
        result = scrape("iphone 12", "Random Company")
        expected_output = "Scraper not available for `Random Company`. Try: eBay, Walmart, or Amazon."
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()

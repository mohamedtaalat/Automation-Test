import time
import unittest
from ddt import ddt, file_data
import pytest
from pages.products_page import ProductPage
from utilities.utility import Utilities

@pytest.mark.usefixtures("driver")
@ddt
class TestProduct(unittest.TestCase):
    @file_data("../test_data/searchbar_data.json")
    def test_check_search_bar(self, item, screenPath):
        product_page = ProductPage(self.driver)
        product_page.search_item(item)
        utl = Utilities()
        utl.take_screenshot(self.driver, ".//screen shots/searchbar/test searchbar with{screenPath}.png")
        #driver.save_screenshot(t".//screen shots/searchbar/test searchbar with{screenPath}.png")
        time.sleep(3)

    def test_check_every_item_in_category(self):
        product_page = ProductPage(self.driver)
        product_page.check_every_item_in_category()
        time.sleep(3)

    def test_check_price_of_items(self):
        product_page = ProductPage(self.driver)
        list_of_price=product_page.check_price_of_items()
        utl=Utilities()
        utl.check_price_of_items(list_of_price)
        time.sleep(3)

    def test_check_specific_product(self):
        product_page = ProductPage(self.driver)
        product_page.check_specific_product()
        time.sleep(3)

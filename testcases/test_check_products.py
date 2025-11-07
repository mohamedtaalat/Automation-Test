import time
import pytest
from pages.products_page import ProductPage
from utilities.utility import Utilities

@pytest.mark.usefixtures("driver")
class TestProduct:
    def test_check_products_with_valid_item(self,driver):
        product_page = ProductPage(driver)
        product_page.search_item("Polo")
        time.sleep(3)

    def test_check_products_with_invalid_item(self,driver):
        product_page = ProductPage(driver)
        product_page.search_item("shorma")
        time.sleep(3)

    def test_check_products_with_empty_feild(self,driver):
        product_page = ProductPage(driver)
        product_page.search_item("")
        time.sleep(3)

    def test_check_every_item_in_category(self,driver):
        product_page = ProductPage(driver)
        product_page.check_every_item_in_category()
        time.sleep(3)

    def test_check_price_of_items(self,driver):
        product_page = ProductPage(driver)
        list_of_price=product_page.check_price_of_items()
        utl=Utilities()
        utl.check_price_of_items(list_of_price)
        time.sleep(3)

    def test_check_specific_product(self,driver):
        product_page = ProductPage(driver)
        product_page.check_specific_product()
        time.sleep(3)

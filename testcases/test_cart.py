import time
import unittest
from ddt import ddt, file_data
import pytest

from pages.cart_page import CartPage
from pages.products_page import ProductPage

@pytest.mark.usefixtures("driver")
@ddt
class TestProduct(unittest.TestCase):
    @file_data("../test_data/add_item_data.json")
    def test_add_to_cart_then_ok(self,item,button):
        pr = ProductPage(self.driver)
        pr.add_item_to_cart_then_ok(item,button)
        time.sleep(3)

    @file_data("../test_data/add_item_data.json")
    def test_add_to_cart_then_view_cart(self,item,button):
        pr = ProductPage(self.driver)
        pr.add_item_to_cart_then_view_cart(item,button)
        time.sleep(3)

    @file_data("../test_data/add_item_data.json")
    def test_remove_item_from_cart(self,item,button):
        cr = CartPage(self.driver)
        cr.add_item_then_remove(item,button)
        time.sleep(3)


    def test_quantity_of_item(self):
        cr = CartPage(self.driver)
        quan=cr.check_quantity()
        assert quan=="2"

    def test_name(self):
        cr = CartPage(self.driver)
        name=cr.get_name_of_item()
        assert name == "Blue Top"


    def test_price(self):
        cr = CartPage(self.driver)
        price = cr.check_price()
        assert price =="Rs. 1000"
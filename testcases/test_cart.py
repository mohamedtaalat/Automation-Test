import time
import unittest
from ddt import ddt, file_data
import pytest
from pages.home_page import HomePage
from utilities.utility import Utilities

@pytest.mark.usefixtures("driver")
@ddt
class TestProduct(unittest.TestCase):
    pass
    # def test_add_to_cart(self):
    #     hm = HomePage(self.driver)
    #     hm.click_add_to_cart()
    #     time.sleep(1)
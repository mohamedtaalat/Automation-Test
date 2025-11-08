import time
import unittest
import pytest
from pages.login_page import LoginPage
from ddt import ddt,  file_data

from utilities.utility import Utilities


@ddt
@pytest.mark.usefixtures("driver")
class TestLogIn(unittest.TestCase):
    @file_data("../test_data/login_data.json")
    def test_log_in(self,email,password,screenPath):
        login_page = LoginPage(self.driver)
        login_page.login(email, password)
        utl = Utilities()
        utl.take_screenshot(self.driver, ".//screen shots/login/login{screenPath}.png")
        #driver.save_screenshot(".//screen shots/login/login{screenPath}.png")
        time.sleep(3)
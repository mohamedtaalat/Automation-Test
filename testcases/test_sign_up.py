import time
import unittest
import pytest
from pages.signup_page import SignUpPage
from ddt import ddt, file_data
from utilities.utility import Utilities

@pytest.mark.usefixtures("driver")
@ddt
class TestSignUp(unittest.TestCase):
    @file_data("../test_data/signup_data.json")
    def test_sign_up(self,name,email,screenPath):
        signup_page = SignUpPage(self.driver)
        signup_page.sign_up(name, email)
        utl = Utilities()
        utl.take_screenshot(self.driver,".//screen shots/signup/sign_up_{screenPath}.png")
        #driver.save_screenshot(".//screen shots/signup/sign_up_{screenPath}.png")
        time.sleep(3)

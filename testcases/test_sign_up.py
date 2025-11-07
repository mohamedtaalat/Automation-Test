import time
import pytest
from pages.signup_page import SignUpPage


@pytest.mark.usefixtures("driver")
class TestSignUp:
    def test_sign_up_with_valid_email(self,driver):
        signup_page = SignUpPage(driver)
        signup_page.sign_up("Mohamed", "test@test")
        #driver.save_screenshot(".//screen shots/signup/sign_up_wrong.png")
        time.sleep(3)

    def test_sign_up_with_invalid_email(self,driver):
        signup_page = SignUpPage(driver)
        signup_page.sign_up("Mohamed", "test@test")
        time.sleep(3)
        #driver.save_screenshot(".//screen shots/signup/sign_up_correct.png")
        time.sleep(3)

    def test_sign_up_with_empty_fields(self, driver):
        signup_page = SignUpPage(driver)
        signup_page.sign_up("", "")
       # driver.save_screenshot(".//screen shots/signup/sign_up_empty.png")
        time.sleep(3)
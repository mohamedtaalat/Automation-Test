import time
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestLogIn:
    def test_log_in_valid_email_password(self,driver):
        login_page = LoginPage(driver)
        login_page.login("test@test","12341234")
       # driver.save_screenshot(".//screen shots/login/login valid email and password")
        time.sleep(3)

    def test_log_in_invalid_email_password(self,driver):
        login_page = LoginPage(driver)
        login_page.login("test@test", "12341234")
        # driver.save_screenshot(".//screen shots/login/login invalid email and password")
        time.sleep(3)

    def test_log_in_invalid_password(self,driver):
        login_page = LoginPage(driver)
        login_page.login("test@test", "12341234")
        # driver.save_screenshot(".//screen shots/login/login valid email and invalid password")
        time.sleep(3)

    def test_log_in_invalid_email(self,driver):
        login_page = LoginPage(driver)
        login_page.login("test@test", "12341234")
        # driver.save_screenshot(".//screen shots/login/login invalid email and valid password")
        time.sleep(3)

    def test_log_in_empty_fields(self,driver):
        login_page = LoginPage(driver)
        login_page.login("", "")
        # driver.save_screenshot(".//screen shots/login/login empty fields")
        time.sleep(3)
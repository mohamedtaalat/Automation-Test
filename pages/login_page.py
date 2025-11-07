from selenium.webdriver.common.by import By
from base import base_init
from pages.home_page import HomePage
from testcases.conftest import driver

class LoginPage(base_init.Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def login(self,email,password):
        home_page = HomePage(self.driver)
        home_page.click_sign_up()
        self.write_email(email)
        self.write_password(password)
        self.click_login()

    def write_email(self,email):
        self.wait_until_visible(By.XPATH,"//input[@data-qa='login-email']").send_keys(email)

    def write_password(self,password):
        self.wait_until_visible(By.XPATH,"//input[@placeholder='Password']").send_keys(password)

    def click_login(self):
        self.wait_until_click(By.XPATH,"//button[normalize-space()='Login']").click()

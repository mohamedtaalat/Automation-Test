from selenium.webdriver.common.by import By
from base import base_init
from pages.home_page import HomePage
from testcases.conftest import driver



class SignUpPage(base_init.Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.home = HomePage(driver)
        self.driver = driver

    def sign_up(self, name, email):
        self.home.click_sign_up()
        self.write_name(name)
        self.write_email(email)
        self.click_signup()

    def write_email(self,email):
        self.wait_until_visible(By.XPATH,"//input[@data-qa='signup-email']").send_keys(email)

    def write_name(self,name):
        self.wait_until_visible(By.XPATH,"//input[@placeholder='Name']").send_keys(name)

    def click_signup(self):
        self.wait_until_click(By.XPATH, "//button[normalize-space()='Signup']").click()